
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect


def home(request):
    return redirect('accounts:login')

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
