from django import forms
from app.models import Contract,Dosmotr


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "number_gtd",
            "reference_gtd",
            "date_recorded",
            "customs_mode",
            "sender",
            "reciever",
            "country",
            "custom_price",
            "factor_price",
            "quantity",
            "status",
        ]

        widgets = {
            'date_recorded': forms.DateInput(attrs={
                'type': 'date',  # HTML5 type date, kalendardan tanlash uchun
            }),
        }


class DosmotrForm(forms.ModelForm):
    class Meta:
        model = Dosmotr
        fields = [
            "number_gtd",
            "reference_gtd",
            "date_recorded",
            "customs_mode",
            "sender",
            "reciever",
            "country",
            "custom_price",
            "factor_price",
            "quantity",
            "status",
        ]

        widgets = {
            'date_recorded': forms.DateInput(attrs={
                'type': 'date',  # HTML5 type date, kalendardan tanlash uchun
            }),
        }

