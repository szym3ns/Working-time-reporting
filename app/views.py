from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, ReportTypeSerializer, ReportSerializer, ProjectSerializer, NotificationStatusSerializer, NotificationSerializer
from app.models import ReportType, Report, Project, NotificationStatus, Notification
from app.forms import ReportTimeForm
from django.shortcuts import redirect
from django.utils import timezone


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ReportTypesViewSet(viewsets.ModelViewSet):
    queryset = ReportType.objects.all().order_by('-name')
    serializer_class = ReportTypeSerializer


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-created')
    serializer_class = ReportSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-name')
    serializer_class = ProjectSerializer


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationStatusesViewSet(viewsets.ModelViewSet):
    queryset = NotificationStatus.objects.all().order_by('-name')
    serializer_class = NotificationStatusSerializer