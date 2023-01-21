from django.shortcuts import render, redirect
from .forms import *
import uuid


def register(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    form = RegistrationForm()
    invite_code = ""
    try:
        invite_code = request.GET['invite_code']
    except:
        pass
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            code = request.POST['ref_code']
            user_invite_code = UserInformation.objects.get(ref_code=code).user
            user_info = UserInformation(user=user, added_by=user_invite_code, ref_code=uuid.uuid4())
            user_info.save()
            return redirect('users:dashboard')
    return render(request, 'registration/register.html', {'form': form, 'invite_code': invite_code})
