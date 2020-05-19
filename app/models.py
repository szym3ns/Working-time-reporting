from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ReportType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']