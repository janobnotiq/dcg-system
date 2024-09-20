from django import forms
from .models import Declaration, Company


class DeclarationForm(forms.ModelForm):
    class Meta:
        model = Declaration
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


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name","phone"]