from dataclasses import field
from pyexpat import model
from django import forms
from .models import *

from django.contrib.auth.models import User


# class DateInput(forms.DateInput):
#     input_type = 'date'
# class TimeInput(forms.TimeInput):
#     input_type = 'time'
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ResidentsInfo
        fields = ('image', 'firstname','middlename','lastname','suffix','sex','phone','birthdate','birthplace','civil_status',
        'citizenship','purok','address','occupation','educ_attainment','single_parent','status','years_resided')



        singParentChoices= (('0','-Select-'),('Yes', 'Yes'),('No', 'No'),)

        widgets = {
            'image' : forms.FileInput(attrs={'class':'form-control', 'id':'file', 'accept':'image/*'}),

            'firstname' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Firstname'}),
            'middlename' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Middlename'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Lastname'}),

            'suffix' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Suffix'}),

            'sex' : forms.Select(attrs={'class':'form-select form-select-sm'}),

            'phone' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'+63'}),
            

            'birthdate' : forms.DateInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Select a date'}),
            'birthplace' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Birthplace'}),

            'civil_status' : forms.Select(attrs={'class':'form-select form-select-sm'}),
            'citizenship' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Citizenship'}),
            'purok' : forms.Select(attrs={'class':'form-select form-select-sm'}),

            'address' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Address'}),

            'occupation' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Occupation'}),

            'educ_attainment' : forms.Select(attrs={'class':'form-select form-select-sm'}),
            'single_parent' : forms.Select(choices=singParentChoices,attrs={'class':'form-select form-select-sm'}),
            'status' : forms.Select(attrs={'class':'form-select form-select-sm'}),

            'years_resided' : forms.DateInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Select a year', 'id':'year'}),
        }
        
    def __init__(self, *args, **kwagrs):
        super(ProfileForm,self).__init__(*args, **kwagrs)
        self.fields['sex'].empty_label = "Select"
        self.fields['civil_status'].empty_label = "Select"
        self.fields['purok'].empty_label = "Select"
        self.fields['educ_attainment'].empty_label = "Select"
        self.fields['status'].empty_label = "Select"
        self.fields['suffix'].required = False

