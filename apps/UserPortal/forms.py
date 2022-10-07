from tkinter import Widget
from django import forms
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class CleranceForm(forms.ModelForm):
    class Meta:
        model = clearance
        fields = ('age', 'purpose')

        widgets = {

            'age' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Age'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'purpose'}),
            
        }


class IndigencyForm(forms.ModelForm):
    class Meta:
        model = CertificateOfIndigency
        fields = ('age', 'purpose')

        widgets = {

            'age' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Age'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'purpose'}),
            
        }

class BuildingPermitForm(forms.ModelForm):
    class Meta:
        model = BuildingPermit
        fields = ('proposed_construction', 'total_area', 'estimated_cost', 'location', 'owner', 'contractor')

        widgets = {

            'proposed_construction' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'total_area' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'estimated_cost' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'location' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'owner' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'contractor' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            
        }

class BusinessPermitForm(forms.ModelForm):
    class Meta:
        model = BusinessPermit
        fields = ('business_name', 'location', 'business_nature', 'owner', 'residece_certificate_no', 'capital_investment', 'gross_sales')

        widgets = {

            'business_name' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'location' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'business_nature' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'owner' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'residece_certificate_no' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'capital_investment' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'gross_sales' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            
        }

class ResidencyCertificateForm(forms.ModelForm):
    class Meta:
        model = ResidencyCertificate
        fields = ('purpose',)
        
        widgets = {
            'purpose' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
        }


class CaptchaPasswordChangeForm(PasswordChangeForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class UpdateUsernameForm(forms.ModelForm):

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ('username',)

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'})
        }

class UpdateEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ('email',)

    