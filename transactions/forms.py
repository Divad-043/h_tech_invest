from django import forms
from .models import Transaction
from accounts.models import User
from django.core.exceptions import ValidationError


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['transaction_uuid', 'date']

    def clean_amount(self):
        # payment_method = self.cleaned_data['payment_method']
        user = self.cleaned_data['user']
        # current_amount = user.total_amount_xaf
        current_amount = user.total_referral_amount_xaf
        data = self.cleaned_data['amount']
        operation = self.cleaned_data['operation']
        if operation == 'WI':
            if data < 3500:
                raise ValidationError('The amount must be greater or egal to 3500')
            else:
                if current_amount < data:
                    raise ValidationError('Error')
                else:
                    data = data - (16*data)/100
        elif operation == 'DE':
            # if payment_method == 'OM' or payment_method == 'MO':
            if data < 5700:
                raise ValidationError('The amount must be greater than 5700')
            first_parent = user.added_by if user.added_by else None
            
            second_parent = None
            if first_parent != None:
                second_parent = first_parent.added_by if first_parent.added_by else None
            third_parent = None
            third_parent = None
            four_parent = None
            if second_parent:
                third_parent = second_parent.added_by if second_parent.added_by else None
            
            if third_parent:
                four_parent = third_parent.added_by if third_parent.added_by else None
            
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
        current_amount = user.total_referral_amount_xaf
        operation = self.cleaned_data['operation']
        if operation == 'WI':
            user.total_referral_amount_xaf = current_amount - self.cleaned_data['amount']
            user.total_amount_withdraw = user.total_amount_withdraw + self.cleaned_data['amount']
        # else:
        #     user.total_amount_xaf = current_amount + self.cleaned_data['amount']
        user.save()
        if commit:
            transaction.save()
        return transaction

