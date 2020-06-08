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
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportTypesViewSet(viewsets.ModelViewSet):
    queryset = ReportType.objects.all().order_by('-name')
    serializer_class = ReportTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-created')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-name')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationStatusesViewSet(viewsets.ModelViewSet):
    queryset = NotificationStatus.objects.all().order_by('-name')
    serializer_class = NotificationStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


def getReportsByUserId(request, idd):
    #try:
    reports = Report.objects.filter(user=idd)
    #except Report.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
    
    alist = {'id' : idd, 'reportsList' : reports}

    return render(request, '../templates/reports.html', alist)


def addReport(request):
    if request.method == 'POST':
        form = ReportTimeForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.created = timezone.now()
            post.save()

    else:
        form = ReportTimeForm()

    return render(request, 'index.html', {'form': form})