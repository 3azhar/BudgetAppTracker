from django import forms

from . models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['merchant', 'description', 'transaction_amount']
        labels = {
            'merchant': 'Merchant',
            'description': 'Description',
            'transaction_amount': 'Transaction Amount'
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80})}

