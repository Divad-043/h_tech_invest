from django.db import models
from accounts.models import User

operation_choices = [
    ('DE', 'Deposit'),
    ('WI', 'Withdraw')
]

payment_method_choices = [
    ('OM', 'Orange Money'),
    ('MO', 'Mtn Money')
]

status_choices = [
    ('Success', 'Success'),
    ('Prepared', 'Prepared'),
    ('Cancel', 'Cancel'),
]

class Transaction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    operation = models.CharField(choices=operation_choices, max_length=2)
    amount = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=4, choices=payment_method_choices)
    status = models.CharField(max_length=10, choices=status_choices)

