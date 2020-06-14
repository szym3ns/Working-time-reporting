from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class ReportType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    budget = models.IntegerField()
    timePredicted = models.IntegerField()
    timeSpent = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class NotificationStatus(models.Model):
    name = models.CharField(max_length=20)


class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    status = models.ForeignKey(NotificationStatus, on_delete=models.CASCADE)


class DailySummary(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reports = models.ManyToManyField(Report)


class MonthlySummary(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reports = models.ManyToManyField(Report)