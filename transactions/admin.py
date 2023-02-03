from django.contrib import admin
from .forms import TransactionForm
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_uuid', 'user', 'amount', 'operation', 'payment_method', 'date', 'status']
    search_fields = ['user__name', 'user__email']
    form = TransactionForm
