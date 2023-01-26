from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Partner, User
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

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
    return render(request, 'users/operations.html', {'page': 'transactions'})


@login_required
def deposit(request):
    return render(request, 'users/deposit.html', {'page': 'deposit'})


@login_required
def withdraw(request):
    return render(request, 'users/withdraw.html', {'page': 'withdraw'})


@login_required
def partners(request):
    current_site = get_current_site(request)
    protocol = "http"
    site_name = current_site.name
    domain = current_site.domain
    list_of_partner = Partner.objects.get(user=request.user).getAllUserPartners()
    list_of_active_partner = [partner for partner in list_of_partner if partner.is_active]
    inactive_partner = len(list_of_partner) - len(list_of_active_partner)
    fisrt_level_user = User.objects.filter(added_by=request.user).count()
    # print(number_of_partners)
    print(list_of_partner)
    context = {
        'page': 'partners', 
        'partners': list_of_partner,
        'first_level_user': fisrt_level_user,
        'protocol': protocol,
        'site_name': site_name,
        'domain': domain,
        'active_partner': list_of_active_partner,
        'inactive_partner': inactive_partner
    }
    return render(request, 'users/partners.html', context)

def settings(request):
    return render(request, 'users/setting.html', {'page': 'settings'})
