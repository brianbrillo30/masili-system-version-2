from django import forms
from django.contrib.auth.models import User



class EditAdminProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'

        )