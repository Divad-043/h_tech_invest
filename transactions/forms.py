from django import forms
from .models import Transaction
from accounts.models import User
from django.core.exceptions import ValidationError


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['transaction_uuid', 'date']

    def clean_amount(self):
        user = self.cleaned_data['user']
        current_amount = user.total_amount_xaf
        data = self.cleaned_data['amount']
        if data > current_amount:
            raise ValidationError('The amount must be less than current amount')
        return data


    def save(self, commit=True):
        transaction =  super().save(commit)
        user = self.cleaned_data['user']
        current_amount = user.total_amount_xaf
        operation = self.cleaned_data['operation']
        # print(self.cleaned_data['amount'])
        # if self.cleaned_data['amount'] > current_amount:
        #     raise ValidationError('The amount must be less than current amount')
        #     print('dedans')
        if operation == 'WI':
            user.total_amount_xaf = current_amount - self.cleaned_data['amount']
        else:
            user.total_amount_xaf = current_amount + self.cleaned_data['amount']
        user.save()
        if commit:
            transaction.save()
        return transaction

