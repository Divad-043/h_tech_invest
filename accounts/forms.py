from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model, password_validation
from .models import Partner, User
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'country', 'phone')


class CodeForm(forms.Form):
    ref_code = forms.UUIDField()

    def clean_ref_code(self):
        data = self.cleaned_data['ref_code']
        try:
            User.objects.get(ref_code=data)
        except ObjectDoesNotExist:
            raise ValidationError("Invalid Code. Enter a valid code", code='invalid_code')
        return data


class AdminAddForm(forms.ModelForm):

    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     super().__init__(*args, **kwargs)

    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'country', 'phone', 'added_by')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            
            print(self.cleaned_data['added_by'])
            partner = Partner.objects.create(user=user)
            if self.cleaned_data['added_by'].user_partner.first_partner_added == None and self.cleaned_data['added_by'].user_partner.last_partern_added == None:
                self.cleaned_data['added_by'].user_partner.first_partern_added = user
                self.cleaned_data['added_by'].user_partner.last_partern_added = user
                
            else:
                last_user_partern_added = self.cleaned_data['added_by'].user_partner.last_partern_added
                last_user_partern_added.user_partner.next_youngest_brother = user
                
           
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone', 'country']


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            "invalid_email": "Enter a valid email"
        }
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    error_messages = {
        "invalid_login": (
            "Please enter a correct email and password."
        ),
        "inactive": "This account is inactive.",
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email is not None and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
        )
