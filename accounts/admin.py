from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AdminUser
from .models import User, Partner
from .forms import RegistrationForm, AdminAddForm


@admin.register(User)
class User(AdminUser):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "ref_code")
    fieldsets = (
        (None, {"fields": ("username", "password", "added_by")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", 'country', 'phone')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('first_name', 'last_name', 'email', 'username', 'country', 'phone', "password1", "password2"),
            },
        ),
    )
    add_form = AdminAddForm()


@admin.register(Partner)
class InfosUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_partern_added', 'last_partern_added', 'next_youngest_brother')

