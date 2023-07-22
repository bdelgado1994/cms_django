from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user=user)
            # messages.success(request, "You Have Been Logged In !")
            return redirect("home")
        else:
            messages.error(
                request, "There was an Error Logging in, Please Try Again..."
            )
            return redirect("home")
    else:
        return render(request, "pages/home.html", {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.error(request, "You Have Been Logged Out")
    return redirect("home")
