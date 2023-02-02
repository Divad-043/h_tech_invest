from django.db import models
from accounts.models import User
import uuid

operation_choices = [
    ('DE', 'Deposit'),
    ('WI', 'Withdraw')
]

payment_method_choices = [
    ('OM', 'Orange Money'),
    ('MO', 'Mtn Money'),
    ('TR', 'Tron'),
    ('US', 'USDT')
]

status_choices = [
    ('Success', 'Success'),
    ('Prepared', 'Prepared'),
    ('Cancel', 'Cancel'),
]

class Transaction(models.Model):
    transaction_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(choices=operation_choices, max_length=2)
    amount = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=4, choices=payment_method_choices)
    #image = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=status_choices)
    date = models.DateTimeField(auto_now=True)

