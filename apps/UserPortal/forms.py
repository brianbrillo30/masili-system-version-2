from django import forms
from .models import *

class CleranceForm(forms.ModelForm):
    class Meta:
        model = clearance
        fields = ('age', 'purpose')

        widgets = {

            'age' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Age'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'purpose'}),
            
        }