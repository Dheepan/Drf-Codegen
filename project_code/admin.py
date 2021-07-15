from django.contrib import admin
from .models import BusinessUnit, Location, Role, User, Manager, Calendar, Event, CalendarSharing, Invitation


#BusinessUnit Admin
class BusinessUnitAdmin(admin.ModelAdmin):
    list_display = [
        'business_unit_id',
        'name',
        'location',
        'registered_address',
        'is_organization',
        'parent_business_unit',
        'parent_org'
        ]


admin.site.register(BusinessUnit, BusinessUnitAdmin)


#Location Admin
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'location_id',
        'name',
        'address',
        'business_unit_id'
        ]


admin.site.register(Location, LocationAdmin)


#Role Admin
class RoleAdmin(admin.ModelAdmin):
    list_display = [
        'role_id',
        'role_name',
        'description',
        'business_unit'
        ]


admin.site.register(Role, RoleAdmin)


#User Admin
class UserAdmin(admin.ModelAdmin):
    list_display = [
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
        'manager'
        ]


admin.site.register(User, UserAdmin)


#Manager Admin
class ManagerAdmin(admin.ModelAdmin):
    list_display = [
        'manager'
        ]


admin.site.register(Manager, ManagerAdmin)


#Calendar Admin
class CalendarAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'name',
        'color'
        ]


admin.site.register(Calendar, CalendarAdmin)


#Event Admin
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'calendar',
        'title',
        'description',
        'timezone',
        'type',
        'start',
        'end'
        ]


admin.site.register(Event, EventAdmin)


#CalendarSharing Admin
class CalendarSharingAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'recipient',
        'calendar',
        'type'
        ]


admin.site.register(CalendarSharing, CalendarSharingAdmin)


#Invitation Admin
class InvitationAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'invitee',
        'event',
        'title',
        'description',
        'type',
        'rvsp',
        'start',
        'end'
        ]


admin.site.register(Invitation, InvitationAdmin)

