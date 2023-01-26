from django.urls import path, reverse_lazy
from django.contrib.auth.urls import views as auth_views
from .forms import LoginForm
from . import views


app_name = 'accounts'
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm, redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("register/invite/?<uuid:invite_code>/", views.register, name="register_with_code"),
    path("register/", views.register, name="register"),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", auth_views.PasswordResetView.as_view(success_url=reverse_lazy("accounts:password_reset_done")), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy("accounts:password_reset_complete")),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("update_user/", views.updateUser, name="update-user"),
    path("update_password/", views.update_password, name="update_password"),
    path("update_user_payment_system/", views.update_user_payment_system, name="update_user_payment_system"),
]
