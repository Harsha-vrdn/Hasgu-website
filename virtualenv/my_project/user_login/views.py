from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        passw = request.POST.get("psw")
        user = authenticate(request, username=uname, password=passw)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("/user_login")
    else:
        return render(request, "authenticate/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Sucessfully logged out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(user)
            messages.success(request, "Created Sucessfully")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "authenticate/register.html", {"form": form})
