# Generated by Django 4.1.5 on 2023-02-02 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_total_amount_bonus_sub_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='total_amount_eth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='total_referral_amount_eth',
        ),
        migrations.AddField(
            model_name='user',
            name='tron_account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='usdt_account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]
