from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def login_user(request):
    """
    Displays a login form for users.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome')
            # Directs user to home page if login is successful.
            return redirect('index')
        else:
            messages.error(request, 'Username/Password do not match')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    """
    View for logging out.
    """
    logout(request)
    messages.success(request, 'Logged out')
    # Directs user to login page if logout is successful.
    return redirect('login')
