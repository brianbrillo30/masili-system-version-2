from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext_lazy as _

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class':'form-control form-control-sm', 'placeholder':'Email'}))
        
    captcha = ReCaptchaField(error_messages={'required': _("You forgot to answer captcha, you're not a robot, right?")})

class CaptchaPasswordResetForm(SetPasswordForm):
    captcha = ReCaptchaField(error_messages={'required': _("You forgot to answer captcha, you're not a robot, right?")})

    
   