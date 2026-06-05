from django import forms
from .models import Record
from categories.models import SubCategory

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['subcategory', 'transaction_type', 'amount', 'remarks']