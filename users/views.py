from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Partner, User
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from transactions.models import Transaction
from transactions.forms import TransactionForm
from services.models import Service
from django.contrib import messages

page = ""

@login_required
def dashboard(request):
    list_of_partner = Partner.objects.get(user=request.user).getAllUserPartners()
    list_of_active_partner = [partner for partner in list_of_partner if partner.is_active]
    inactive_partner = len(list_of_partner) - len(list_of_active_partner)
    user_infos = Partner.objects.get(user=request.user).getTotalNumberOfParternsByLevel(level=2)
    context = {
        'page': 'dashboard',
        'active_partner': list_of_active_partner,
        'inactive_partner': inactive_partner,
        'partners': list_of_partner,
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def transactions(request):
    user = request.user
    user_transactions = Transaction.objects.filter(user=user)
    context = {
        'page': 'transactions',
        'user_transactions': user_transactions
    }
    return render(request, 'users/operations.html', context)


@login_required
def deposit(request):
    services = Service.objects.all()
    form = TransactionForm()
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        print('test')
        data = {
            'image': request.FILES['image'],
            'amount': request.POST['amount'],
            'payment_method': request.POST['payment_method'],
            'user': request.user,
            'operation': 'DE',
            'status': 'Prepared'
        }
        print(data)
        form = TransactionForm(data)
        if form.is_valid():
            print('oui')
            transaction = form.save(commit=False)
            transaction.image = request.FILES['image']
            transaction.save()
            messages.success(request, "Deposit success")
            return redirect('users:deposit')
            
    return render(request, 'users/deposit.html', {'page': 'deposit', 'services': services, 'form': form})


@login_required
def withdraw(request):
    services = Service.objects.all()
    form = TransactionForm()
    if request.method == 'POST':
        print('test')
        data = {
            'phone_to_send': request.POST['phone_to_send'],
            'amount': request.POST['amount'],
            'payment_method': request.POST['payment_method'],
            'user': request.user,
            'operation': 'WI',
            'status': 'Prepared'
        }
        print(data)
        form = TransactionForm(data)
        if form.is_valid():
            print('oui')
            transaction = form.save(commit=False)
            transaction.save()
            messages.success(request, "Withdraw success")
            return redirect('users:deposit')
    return render(request, 'users/withdraw.html', {'page': 'withdraw', 'services': services, 'form': form})


@login_required
def partners(request):
    #level = request.GET['level'] if request.GET['level'] else ""
    level = "ALL"
    try:
        level = request.GET['level']
        level = int(level)
    except:
        pass
    current_site = get_current_site(request)
    protocol = "http"
    site_name = current_site.name
    domain = current_site.domain
    list_of_partner = Partner.objects.get(user=request.user).getAllUserPartners()
    # partners = [partner for partner in list_of_partner]
    if level == 1 or level == 2 or level == 3 or level ==4:
        level_partners = Partner.objects.get(user=request.user).getAllUsersByLevel(level)
    else:
        level_partners = [partner for partner in list_of_partner]

    list_of_active_partner = [partner for partner in list_of_partner if partner.is_active]
    inactive_partner = len(list_of_partner) - len(list_of_active_partner)
    fisrt_level_user = User.objects.filter(added_by=request.user).count()
    # print(number_of_partners)
    print(list_of_partner)
    context = {
        'page': 'partners', 
        'partners': list_of_partner,
        'level_partners': level_partners,
        'first_level_user': fisrt_level_user,
        'protocol': protocol,
        'site_name': site_name,
        'domain': domain,
        'active_partner': list_of_active_partner,
        'inactive_partner': inactive_partner,
        'level': level
    }
    return render(request, 'users/partners.html', context)

def settings(request):
    return render(request, 'users/setting.html', {'page': 'settings'})


def filter_by_level(request):
    level = request.GET['level']
    level = int(level)
    user = request.user
    partner = Partner.objects.filter(user=user)
    # all_level_partner = partner.getTotalNumberOfParternsByLevel(level)
    all_partner = Partner.objects.get(user=request.user).getAllUserPartners()
    list_of_partner = Partner.objects.get(user=request.user).getAllUsersByLevel(level)
    list_of_active_partner = [partner for partner in all_partner if partner.is_active]
    inactive_partner = len(all_partner) - len(list_of_active_partner)
    fisrt_level_user = User.objects.filter(added_by=request.user).count()

    context = {
        'page': 'partners', 
        'partners': all_partner,
        'level_partner': list_of_partner,
        'first_level_user': fisrt_level_user,
        'active_partner': list_of_active_partner,
        'inactive_partner': inactive_partner
    }
    return render(request, 'users/partners.html', context)

