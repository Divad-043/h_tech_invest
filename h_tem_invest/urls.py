
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
]
