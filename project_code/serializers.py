from rest_framework import serializers
from .models import  BusinessUnit, Location, Role, User, Manager, Calendar, Event, CalendarSharing, Invitation


#BusinessUnit Serializer
class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = (
        'business_unit_id',
        'name',
        'location',
        'registered_address',
        'is_organization',
        'parent_business_unit',
        'parent_org',
        )


#Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
        'location_id',
        'name',
        'address',
        'business_unit_id',
        )


#Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
        'role_id',
        'role_name',
        'description',
        'business_unit',
        )


#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'employee_id',
        'first_name',
        'last_name',
        'picture',
        'gender',
        'business_unit',
        'location',
        'email',
        'date_joined',
        'date_of_birth',
        'age',
        'phone_number',
        'alternative_phone_number',
        'permanent_address',
        'current_address',
        'about_me',
        'role',
        'is_staff',
        'is_active',
        'is_organization_admin',
        'manager',
        )


#Manager Serializer
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = (
        'manager',
        )


#Calendar Serializer
class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = (
        'owner',
        'name',
        'color',
        )


#Event Serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
        'calendar',
        'title',
        'description',
        'timezone',
        'type',
        'start',
        'end',
        )


#CalendarSharing Serializer
class CalendarSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarSharing
        fields = (
        'owner',
        'recipient',
        'calendar',
        'type',
        )


#Invitation Serializer
class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = (
        'owner',
        'invitee',
        'event',
        'title',
        'description',
        'type',
        'rvsp',
        'start',
        'end',
        )

