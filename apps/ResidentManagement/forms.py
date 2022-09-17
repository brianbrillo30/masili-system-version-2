from django import forms
from .models import *

# class DateInput(forms.DateInput):
#     input_type = 'date'
# class TimeInput(forms.TimeInput):
#     input_type = 'time'
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ResidentsInfo
        fields = ('image', 'firstname','middlename','lastname','suffix','sex','phone','email','birthdate','birthplace','civil_status',
        'citizenship','purok','address','occupation','educ_attainment','single_parent','status')



        singParentChoices= (('0','-Select-'),('1', 'Yes'),('2', 'No'),)

        widgets = {
            'image' : forms.FileInput(attrs={'class':'form-control', 'id':'file', 'accept':'image/*'}),

            'firstname' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Firstname'}),
            'middlename' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Middlename'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Lastname'}),

            'suffix' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Suffix'}),

            'sex' : forms.Select(attrs={'class':'form-select form-select-sm'}),

            'phone' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'+63'}),
            'email' : forms.EmailInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Email'}),

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
        }
        
    def __init__(self, *args, **kwagrs):
        super(ProfileForm,self).__init__(*args, **kwagrs)
        self.fields['sex'].empty_label = "Select"
        self.fields['civil_status'].empty_label = "Select"
        self.fields['purok'].empty_label = "Select"
        self.fields['educ_attainment'].empty_label = "Select"
        self.fields['status'].empty_label = "Select"
        self.fields['suffix'].required = False