from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/transactions', views.transactions, name='transactions'),
    path('dashboard/deposit', views.deposit, name='deposit'),
    path('dashborad/withdraw', views.withdraw, name='withdraw'),
    path('dashboard/partners', views.partners, name='partners'),
    path('dashboard/settings', views.settings, name='settings')
]