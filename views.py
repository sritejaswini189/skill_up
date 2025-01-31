from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages  # Import messages framework
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user to database
            messages.success(request, "Successfully Registered! Please log in.")  # Success message
            return redirect('login')  # Redirect to login page
        else:
            messages.error(request, "Registration failed. Please check the form.")  # Error message
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")  # Success message
                return redirect('courses')  # Redirect to courses page
            else:
                messages.error(request, "Invalid username or password.")  # Error message
        else:
            messages.error(request, "Invalid username or password.")  # Error message

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def courses(request):
    return render(request, 'users/courses.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")  # Logout message
    return redirect('home')  # Redirect to home page

def branch(request):
    return render(request, 'users/branch.html')

def cse(request):
    return render(request,'users/cse.html')

def ece(request):
    return render(request,'users/ece.html')

def java(request):
    return render(request,'users/java.html')

def python(request):
    return render(request,'users/python.html')

def html_css(request):
    return render(request,'users/html_css.html')

def analog(request):
    return render(request,'users/analog.html')

def control(request):
    return render(request,'users/control.html')
