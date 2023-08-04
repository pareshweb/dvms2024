from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, " You have been logged In !! ")
            return redirect('home')  # Redirect to a dashboard page upon successful login
        else:
            # Display an error message for unsuccessful login
            messages.success(request, " There was an error Logging In , Please try again....!! ")
            return redirect('home')
    
    else:
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, " You have been logged out !! ")
    return redirect('home')

