from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


    def save(self, commit=True):
        admin = super(AdminRegistrationForm, self).save(commit=False)
        admin.first_name = self.cleaned_data['first_name']
        admin.last_name = self.cleaned_data['last_name']
        admin.email = self.cleaned_data['email']

        
        if commit:
            admin.save()

        return admin
