from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/",CustomLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("register/",RegisterPage.as_view(),name="register"),
]
