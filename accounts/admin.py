from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AdminUser
from .models import User, UserInformation
from .forms import RegistrationForm


@admin.register(User)
class User(AdminUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('first_name', 'last_name', 'email', 'username', 'country', 'phone', "password1", "password2"),
            },
        ),
    )
    add_form = RegistrationForm


@admin.register(UserInformation)
class InfosUserAdmin(admin.ModelAdmin):
    list_display = ('ref_code', 'user', 'added_by')

