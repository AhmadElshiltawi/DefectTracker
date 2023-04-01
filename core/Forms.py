from django import forms
from django.forms import ModelForm
from .models import Bug


##create a form for bug

class BugForm(ModelForm):
    class Meta:
        model  = Bug
        fields = ('date', 'title', 'description', 'project_id', 'user')
