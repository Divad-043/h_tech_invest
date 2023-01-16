from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserInfos

admin.site.register(User, UserAdmin)


@admin.register(UserInfos)
class InfosUserAdmin(admin.ModelAdmin):
    list_display = ('ref_code', 'user', 'added_by')
