from dataclasses import fields
from django.forms import ModelForm
from apps.AnnouncementManagement.models import Announcement
from django import forms

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(),
            'body' : forms.Textarea(),
            'image' : forms.FileInput(attrs={'class':'form-control', 'id':'file-2', 'accept':'image/*'}),
        }

