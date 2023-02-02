from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transactions/', views.transactions, name='transactions'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('partners/', views.partners, name='partners'),
    path('settings/', views.settings, name='settings'),
    path('filter_by_level/', views.filter_by_level, name='filter_by_level')
]