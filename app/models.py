from django.db import models

# Create your models here.


class ReportType(models.Model):
    name = models.CharField(max_length=30)


class Report(models.Model):
    type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()

    class Meta:
        ordering = ['created']