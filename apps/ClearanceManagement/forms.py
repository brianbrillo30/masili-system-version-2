from django import forms
from apps.UserPortal.models import*

class cleranceForm(forms.ModelForm):
    class Meta:
        model = clearance
        fields = ('age', 'purpose', 'status', 'date_released')

        widgets = {

            'age' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Age'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'purpose'}),
            'date_released' : forms.DateInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            'status' : forms.Select(attrs={'class':'form-select form-select-sm'}),
            
        }

    def __init__(self, *args, **kwagrs):
        super(cleranceForm,self).__init__(*args, **kwagrs)
        self.fields['date_released'].required = False