from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import ReportType, Report, Notification, NotificationStatus, Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ReportTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportType
        fields = ['name']


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ['type', 'description', 'created', 'time', 'user']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'budget', 'timePredicted', 'timeSpent']


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['created', 'author', 'description', 'status']

    def to_representation(self, instance):
        rep = super(NotificationSerializer, self).to_representation(instance)
        rep['author'] = instance.author.id
        return rep


class NotificationStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationStatus
        fields = ['name']