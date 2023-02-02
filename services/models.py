from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=100)
    name_account = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
