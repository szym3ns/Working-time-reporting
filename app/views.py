from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, ReportTypeSerializer, ReportSerializer, ProjectSerializer, NotificationStatusSerializer, NotificationSerializer
from app.models import ReportType, Report, Project, NotificationStatus, Notification
from app.forms import ReportTimeForm
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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


@api_view(['GET'])
def getUserById(request, pk):
    user = User.objects.get(id=pk)

    serializer_context = {
        'request': request,
    }
    serializer = UserSerializer(user, context=serializer_context)
    return Response(serializer.data)


@api_view(['GET'])
def getNotificationByUserId(request, pk):
    notification = Notification.objects.filter(author=pk)

    serializer_context = {
        'request': request,
    }
    serializer = NotificationSerializer(notification, many=True, context=serializer_context)
    return Response(serializer.data)


@api_view(['GET'])
def getNotificationByDate(request, year, month, day, hour, minute, second):
    notification = Notification.objects.filter( created__year=year, 
                                                created__month=month, 
                                                created__day=day, 
                                                created__hour=hour, 
                                                created__minute=minute, 
                                                created__second=second)

    serializer_context = {
        'request': request,
    }
    serializer = NotificationSerializer(notification, many=True, context=serializer_context)
    return Response(serializer.data)