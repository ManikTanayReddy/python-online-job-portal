from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import JobSeekerForm, RecruiterForm

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def jobseeker_register(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic for jobseeker registration if needed
            return redirect('jobseeker_login')
    else:
        form = JobSeekerForm()
    context = {'form': form}
    return render(request, 'jobseeker_register.html', context)

def jobseeker_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('jobseeker_dashboard')  # Redirect to jobseeker dashboard after login
    return render(request, 'jobseeker_login.html')

def jobseeker_logout(request):
    logout(request)
    return redirect('jobseeker_login')  # Redirect to jobseeker login after logout

def recruiter_register(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic for recruiter registration if needed
            return redirect('recruiter_login')
    else:
        form = RecruiterForm()
    context = {'form': form}
    return render(request, 'recruiter_register.html', context)

def recruiter_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recruiter_dashboard')  # Redirect to recruiter dashboard after login
    return render(request, 'recruiter_login.html')

def recruiter_logout(request):
    logout(request)
    return redirect('recruiter_login')  # Redirect to recruiter login after logout
