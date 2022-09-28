from django import forms
from apps.UserPortal.models import*

class BuildingPermitForm(forms.ModelForm):
    class Meta:
        model = BuildingPermit
        fields = ('proposed_construction', 'total_area', 'estimated_cost', 'location', 'owner', 'contractor', 'prepared_by', 'paid_under_or', 'date_released', 'amount_paid', 'status')

        widgets = {

            'proposed_construction' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'total_area' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'estimated_cost' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'location' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'owner' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'contractor' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),

            'prepared_by' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),

            'paid_under_or' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),
            'date_released' : forms.DateInput(attrs={'class':'form-control form-control-sm', 'placeholder':'input'}),
            'amount_paid' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Input'}),

            'status' : forms.Select(attrs={'class':'form-select form-select-sm'}),
        }

    def __init__(self, *args, **kwagrs):
        super(BuildingPermitForm,self).__init__(*args, **kwagrs)
        self.fields['prepared_by'].required = False
        self.fields['paid_under_or'].required = False
        self.fields['date_released'].required = False
        self.fields['amount_paid'].required = False