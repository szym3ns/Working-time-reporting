from django import forms
from app.models import Report


class ReportTimeForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('type', 'description', 'time', 'user')
