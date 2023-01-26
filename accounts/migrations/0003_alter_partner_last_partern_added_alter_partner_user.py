# Generated by Django 4.1.5 on 2023-01-23 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='last_partern_added',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_partner_added', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partner',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_partner', to=settings.AUTH_USER_MODEL),
        ),
    ]
