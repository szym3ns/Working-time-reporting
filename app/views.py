from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import *
from app.models import *
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


class DailySummaryViewSet(viewsets.ModelViewSet):
    queryset = DailySummary.objects.all()
    serializer_class = DailySummarySerializer


@api_view(['GET'])
def getUserById(request, pk):
    user = User.objects.get(id=pk)

    serializer_context = {
        'request': request,
    }
    serializer = UserSerializer(user, context=serializer_context)
    return Response(serializer.data)


@api_view(['GET'])
def getReportByUserId(request, pk):
    report = Report.objects.filter(user=pk)

    serializer_context = {
        'request': request,
    }
    serializer = ReportSerializer(report, many=True, context=serializer_context)
    return Response(serializer.data)


@api_view(['GET'])
def getReportByDate(request, year, month, day, hour, minute, second):
    report = Report.objects.filter( created__year=year, 
                                                created__month=month, 
                                                created__day=day, 
                                                created__hour=hour, 
                                                created__minute=minute, 
                                                created__second=second)

    serializer_context = {
        'request': request,
    }
    serializer = ReportSerializer(report, many=True, context=serializer_context)
    return Response(serializer.data)