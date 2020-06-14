from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'groups']


class ReportTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportType
        fields = ['name']


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ['type', 'description', 'created', 'time', 'user', 'project']

    def to_representation(self, instance):
        report = super(ReportSerializer, self).to_representation(instance)
        report['user'] = instance.user.id
        report['project'] = instance.project.name
        report['type'] = instance.type.name

        return report


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'budget', 'timePredicted', 'timeSpent']


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'created', 'author', 'description', 'status']

    def to_representation(self, instance):
        notification = super(NotificationSerializer, self).to_representation(instance)
        notification['author'] = instance.author.id
        
        return notification


class NotificationStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationStatus
        fields = ['name']


class DailySummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DailySummary
        fields = ['created', 'employee', 'reports']

    def to_representation(self, instance):
        summary = super(DailySummarySerializer, self).to_representation(instance)
        summary['employee'] = instance.employee.id
        
        return summary