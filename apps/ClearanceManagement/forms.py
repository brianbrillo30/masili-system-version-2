from django import forms
from apps.UserPortal.models import*

class cleranceForm(forms.ModelForm):
    class Meta:
        model = clearance
        fields = ('age', 'purpose', 'status', 'date_released','community_tax_num', 'community_tax_date_issued')

        widgets = {

            'age' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            'date_released' : forms.DateInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            'status' : forms.Select(attrs={'class':'form-select form-select-sm'}),
            'community_tax_num' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            'community_tax_date_issued' : forms.DateInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            
        }

    def __init__(self, *args, **kwagrs):
        super(cleranceForm,self).__init__(*args, **kwagrs)
        self.fields['date_released'].required = False
        self.fields['community_tax_num'].required = False
        self.fields['community_tax_date_issued'].required = False