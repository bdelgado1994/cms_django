from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm
from .models import Record


def home(request):
    records=Record.objects.all()
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
        return render(request, "pages/home.html", {"records":records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.error(request, "You Have Been Logged Out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Resgistered! Welcome")
            return redirect("home")
    else:
        form = SingUpForm()
        return render(request, "pages/register.html", {"form": form})
    return render(request, "pages/register.html", {"form": form})
