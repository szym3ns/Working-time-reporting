from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import ReportType, Report


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