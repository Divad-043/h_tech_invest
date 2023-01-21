from django.shortcuts import render
from django.contrib.auth.decorators import login_required

page = ""

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {'page': 'dashboard'})


@login_required
def transactions(request):
    return render(request, 'users/operations.html', {'page': 'transactions'})


@login_required
def deposit(request):
    return render(request, 'users/deposit.html', {'page': 'deposit'})


@login_required
def withdraw(request):
    return render(request, 'users/withdraw.html', {'page': 'withdraw'})


@login_required
def partners(request):
    return render(request, 'users/partners.html', {'page': 'partners'})

def settings(request):
    return render(request, 'users/setting.html', {'page': 'settings'})
