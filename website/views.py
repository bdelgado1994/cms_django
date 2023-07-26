from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
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
        return render(request, "pages/home.html", {"records": records})


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


def costumer_record(request, pk):
    if request.user.is_authenticated:
        costumer_records = Record.objects.get(id=pk)
        return render(
            request, "pages/record.html", {"costumer_records": costumer_records}
        )
    else:
        messages.error(request, "You Must Be Logged In To View That Page..")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete = delete_it
        messages.error(request, f"Record {delete} has been deleted successfully")
        delete_it.delete()
        return redirect("home")
    else:
        messages.error(request, "You Must Be Logged In To View That Page..")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("home")
        return render(request, "pages/add_recod.html", {"form": form})
    else:
        messages.error(request, "You Must Be Logged In To View That Page..")
        return redirect("home")

def update_record(request,pk):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "pages/update_recod.html", {"form": form})
    else:
        messages.error(request, "You Must Be Logged In To View That Page..")
        return redirect("home")    
