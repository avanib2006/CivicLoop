from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )

        user.profile.role = role
        user.profile.save()

        login(request, user)

        if role == "authority":
            return redirect("authority_dashboard")

        return redirect("citizen_dashboard")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)

            if hasattr(user, "profile") and user.profile.role == "authority":
                return redirect("authority_dashboard")

            return redirect("citizen_dashboard")

        messages.error(request, "Invalid email or password.")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")
def citizen_dashboard(request):
    return render(request, "citizen_dashboard.html")


def authority_dashboard(request):
    return render(request, "authority_dashboard.html")