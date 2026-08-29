from django.contrib import admin
from django.urls import path
from .views import home
from users.views import (
    register,
    login_view,
    logout_view,
    citizen_dashboard,
    authority_dashboard,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
    "citizen-dashboard/",
    citizen_dashboard,
    name="citizen_dashboard"
),

path(
    "authority-dashboard/",
    authority_dashboard,
    name="authority_dashboard"
),
]