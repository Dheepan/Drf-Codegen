from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BusinessUnit, Location, Role, User, Manager, Calendar, Event, CalendarSharing, Invitation


#BusinessUnit retrieve API view
class BusinessUnitRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BusinessUnitSerializer

    def get_queryset(self):
        return BusinessUnit.objects.all()

#BusinessUnit list API view
class BusinessUnitListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BusinessUnitSerializer

    def get_queryset(self):
        return BusinessUnit.objects.all()

#BusinessUnit update API view
class BusinessUnitUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BusinessUnitSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = BusinessUnitSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#Location retrieve API view
class LocationRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()

#Location list API view
class LocationListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()

#Location update API view
class LocationUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = LocationSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#Role retrieve API view
class RoleRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.all()

#Role list API view
class RoleListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.all()

#Role update API view
class RoleUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = RoleSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#User retrieve API view
class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

#User list API view
class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

#User update API view
class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#Manager retrieve API view
class ManagerRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ManagerSerializer

    def get_queryset(self):
        return Manager.objects.all()

#Manager list API view
class ManagerListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ManagerSerializer

    def get_queryset(self):
        return Manager.objects.all()

#Manager update API view
class ManagerUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ManagerSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = ManagerSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#Calendar retrieve API view
class CalendarRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSerializer

    def get_queryset(self):
        return Calendar.objects.all()

#Calendar list API view
class CalendarListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSerializer

    def get_queryset(self):
        return Calendar.objects.all()

#Calendar update API view
class CalendarUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = CalendarSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#Event retrieve API view
class EventRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

#Event list API view
class EventListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

#Event update API view
class EventUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = EventSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#CalendarSharing retrieve API view
class CalendarSharingRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSharingSerializer

    def get_queryset(self):
        return CalendarSharing.objects.all()

#CalendarSharing list API view
class CalendarSharingListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSharingSerializer

    def get_queryset(self):
        return CalendarSharing.objects.all()

#CalendarSharing update API view
class CalendarSharingUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSharingSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = CalendarSharingSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#Invitation retrieve API view
class InvitationRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvitationSerializer

    def get_queryset(self):
        return Invitation.objects.all()

#Invitation list API view
class InvitationListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvitationSerializer

    def get_queryset(self):
        return Invitation.objects.all()

#Invitation update API view
class InvitationUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvitationSerializer

    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = InvitationSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
