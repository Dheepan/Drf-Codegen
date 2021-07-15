from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import TimeStampedModel
from .managers import UserManager
from datetime import date
from computed_property import ComputedIntegerField
from django.utils.timezone import now
from django.utils import timezone as _timezone
from pytz import all_timezones
from django.conf.global_settings import TIME_ZONE


class BusinessUnit(TimeStampedModel):
    business_unit_id = models.IntegerField(default=-1, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    registered_address = models.TextField()
    is_organization = models.BooleanField(default=False)
    parent_business_unit = models.ForeignKey('self', default=-1, on_delete=models.PROTECT, blank=True, null=True,
                                             to_field='business_unit_id')
    parent_org = models.ForeignKey('self', default=-1, on_delete=models.PROTECT, blank=True, null=True,
                                   related_name='+', to_field='business_unit_id')

    def __str__(self):
        return self.name


class Location(TimeStampedModel):
    location_id = models.IntegerField(default=-1, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, default='No Location')
    address = models.TextField(max_length=500)
    business_unit_id = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT, related_name='+',
                                         to_field='business_unit_id')

    def __str__(self):
        return self.name


class Role(TimeStampedModel):
    role_id = models.IntegerField(default=-1, unique=True)
    role_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    business_unit = models.ForeignKey(BusinessUnit, blank=True, null=True, on_delete=models.PROTECT,
                                      to_field='business_unit_id')

    def __str__(self):
        return self.role_name


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    employee_id = models.CharField(max_length=10, default='')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    picture = models.ImageField(blank=True, null=True, default='media/default.png')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, default='M')
    business_unit = models.ForeignKey(BusinessUnit, null=True, blank=True, on_delete=models.PROTECT,
                                      to_field='business_unit_id')
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.PROTECT, to_field='location_id')
    email = models.EmailField(max_length=40, unique=True)
    date_joined = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, default=now)
    age = ComputedIntegerField(compute_from='calculate_age', default=0)

    @property
    def calculate_age(self):
        born = self.date_of_birth
        today = date.today()
        calculated_age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return calculated_age

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    alternative_phone_number = models.CharField(max_length=15, null=True, blank=True)
    permanent_address = models.TextField(max_length=400, blank=True, null=True)
    current_address = models.TextField(max_length=400, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True, max_length=500)
    role = models.ForeignKey(Role, null=True, on_delete=models.PROTECT, blank=True, to_field='role_id')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_organization_admin = models.BooleanField(default=False)
    manager = models.ForeignKey('Manager', blank=True, null=True, on_delete=models.PROTECT, related_name='employee')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_picture(self):
        if self.picture:
            return self.picture.url

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class Manager(models.Model):
    manager = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='+')

    def __str__(self):
        return self.manager.email


class Calendar(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class EventMixin(object):
    NORMAL = 'NM'
    ALL_DAY = 'AD'
    TYPE_CHOICES = (
        (NORMAL, 'Normal'),
        (ALL_DAY, 'All Day'),
    )


class Event(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    description = models.TextField()
    timezone = models.CharField(max_length=50, choices=((x, x) for x in all_timezones), default=TIME_ZONE)
    type = models.CharField(max_length=2, choices=EventMixin.TYPE_CHOICES, default=EventMixin.NORMAL)
    start = models.DateTimeField(default=_timezone.now)
    end = models.DateTimeField(default=_timezone.now)

    def __str__(self):
        return self.title


class CalendarSharing(models.Model):
    READ = 'R'
    WRITE = 'W'
    TYPE_CHOICES = (
        (READ, 'READ'),
        (WRITE, 'WRITE'),
    )

    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sharing_owner')
    recipient = models.ForeignKey(User, on_delete=models.PROTECT)
    calendar = models.ForeignKey(Calendar, on_delete=models.PROTECT)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=READ)

    class Meta:
        unique_together = ('recipient', 'calendar')


class Invitation(models.Model):
    UNKNOWN = 'u'
    MAYBE = 'm'
    YES = 'y'
    NO = 'n'
    RVSP_CHOICES = (
        (UNKNOWN, 'UNKNOWN'),
        (MAYBE, 'MAYBE'),
        (YES, 'YES'),
        (NO, 'NO'),
    )

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    invitee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='invitee')
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='invited_to')
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=2, choices=EventMixin.TYPE_CHOICES, default=EventMixin.NORMAL,
                            blank=True, null=True)
    rvsp = models.CharField(max_length=1, choices=RVSP_CHOICES, default=UNKNOWN, blank=True, null=True)
    start = models.DateTimeField(default=_timezone.now)
    end = models.DateTimeField(default=_timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('invitee', 'event')
