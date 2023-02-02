from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=100)
