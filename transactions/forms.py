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
        operation = self.cleaned_data['operation']
        # if data > current_amount:
        #     raise ValidationError('The amount must be less than current amount')
        if operation == 'WI':
            if data < 3500:
                raise ValidationError('The amount must be greater or egal to 3500')
        elif operation == 'DE':
            if data < 5700:
                raise ValidationError('The amount must be greater than 5700')
            first_parent = user.added_by if user.added_by else None
            #print(first_parent)
            second_parent = None
            if first_parent != None:
                second_parent = first_parent.added_by if first_parent.added_by else None
            #print(second_parent)
            third_parent = None
            third_parent = None
            four_parent = None
            if second_parent:
                third_parent = second_parent.added_by if second_parent.added_by else None
            #print(third_parent)
            if third_parent:
                four_parent = third_parent.added_by if third_parent.added_by else None
            #print(four_parent)


            if first_parent:
                first_parent.total_referral_amount_xaf += 1000
                first_parent.save()
            if second_parent:
                second_parent.total_referral_amount_xaf += 500
                second_parent.save()
            if third_parent:
                third_parent.total_referral_amount_xaf += 250
                third_parent.save()
            if four_parent:
                four_parent.total_referral_amount_xaf += 125
                four_parent.save()
        else:
            raise ValidationError('Nothing to do')
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
            user.total_amount_withdraw = user.total_amount_withdraw + self.cleaned_data['amount']
        else:
            user.total_amount_xaf = current_amount + self.cleaned_data['amount']
        user.save()
        if commit:
            transaction.save()
        return transaction

