# Generated by Django 4.1.5 on 2023-02-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_transaction_status_alter_transaction_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='phone_to_send',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]