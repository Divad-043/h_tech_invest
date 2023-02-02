from django.shortcuts import render, redirect
from .forms import *
from .models import User, Partner
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


def register(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    form = RegistrationForm()
    invite_code = ""
    try:
        invite_code = request.GET['inviteCode']
    except:
        pass
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            code = request.POST['ref_code']
            user_invite_code = User.objects.get(ref_code=code)
            user.added_by = user_invite_code
            user.save()
            if user_invite_code.user_partner.first_partern_added == None and user_invite_code.user_partner.last_partern_added == None:
                user_invite_code.user_partner.first_partern_added = user
                user_invite_code.user_partner.last_partern_added = user
                user_invite_code.save()
            else:
                last_user_partern_added = user_invite_code.user_partner.last_partern_added
                last_user_partern_added.user_partner.next_youngest_brother = user
                last_user_partern_added.save()
            partner = Partner(user=user)
            partner.save()
            return redirect('accounts:login')
    return render(request, 'registration/register.html', {'form': form, 'invite_code': invite_code})

@login_required
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your informations has been updated successfully")
            return redirect("users:settings")
        message = "An Error Occured. Please try again and verify your informations"
    return render(request, 'users/setting.html', {"message": message})

@login_required
def update_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            print("oui")
            form.save()
            messages.success(request, "Your password has been updated successfully")
            return redirect("users:settings")
    return render(request, 'users/setting.html')

@login_required
def update_user_payment_system(request):
    form = UpdatePaymentAccount()
    user = request.user
    if request.method == 'POST':
        form = UpdatePaymentAccount(request.POST)
        print('ok')
        if form.is_valid():
            print('valid')
            user.usdt_account_number = form.cleaned_data['tron_acc']
            user.tron_account_number = form.cleaned_data['usdt_acc']
            user.save()
            messages.success(request, "Your account number has been updated successfully")
            return redirect("users:settings")
    return render(request, 'users/setting.html')