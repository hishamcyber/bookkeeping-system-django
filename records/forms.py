from django import forms
from .models import Record
from categories.models import MainCategory, SubCategory

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['main_category', 'subcategory', 'transaction_type', 'amount', 'remarks']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['main_category'].queryset = MainCategory.objects.filter(user=user)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(user=user)
            self.fields['subcategory'].required = False