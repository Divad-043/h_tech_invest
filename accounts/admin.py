from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserInformation

admin.site.register(User, UserAdmin)


@admin.register(UserInformation)
class InfosUserAdmin(admin.ModelAdmin):
    list_display = ('ref_code', 'user', 'added_by')
