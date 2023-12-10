from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        candidates=Candidate.objects.filter(company__name=request.user.username)
        context={
            'candidates':candidates,
        }
        return render(request,'hr.html',context)
    else:
        companies=Company.objects.all()
        context={
            'companies':companies,
        }
        return render(request,'Jobseeker.html',context)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import JobSeekerRegistrationForm, RecruiterRegistrationForm

# Existing views...

def jobseeker_register(request):
    if request.method == 'POST':
        form = JobSeekerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic for jobseeker registration if needed
            return redirect('jobseeker_login')
    else:
        form = JobSeekerRegistrationForm()
    context = {'form': form}
    return render(request, 'jobseeker_register.html', context)

def jobseeker_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or any other page after login
    return render(request, 'jobseeker_login.html')

def jobseeker_logout(request):
    logout(request)
    return redirect('jobseeker_login')  # Redirect to the login page for job seekers

def recruiter_register(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Additional logic for recruiter registration if needed
            return redirect('recruiter_login')
    else:
        form = RecruiterRegistrationForm()
    context = {'form': form}
    return render(request, 'recruiter_register.html', context)

def recruiter_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or any other page after login
    return render(request, 'recruiter_login.html')

def recruiter_logout(request):
    logout(request)
    return redirect('recruiter_login')  # Redirect to the login page for recruiters



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CandidateForm, RecruiterForm, CompanyForm
from .models import Candidate, Company, Recruiter

# Your existing views here...

def candidateProfile(request):
    candidate, created = Candidate.objects.get_or_create(user=request.user)  # Retrieve or create candidate profile

    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or any other page
    else:
        form = CandidateForm(instance=candidate)
    context = {'form': form}
    return render(request, 'candidate_profile.html', context)

def recruiterProfile(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            recruiter = form.save(commit=False)
            recruiter.user = request.user  # Assuming user is authenticated
            recruiter.save()
            return redirect('home')  # Redirect to home or any other page
    else:
        form = RecruiterForm()
    context = {'form': form}
    return render(request, 'recruiter_profile.html', context)


def companyProfile(request):
    company = Company.objects.get(admin=request.user)  # Assuming the logged-in user is the admin
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or any other page
    else:
        form = CompanyForm(instance=company)
    context = {'form': form}
    return render(request, 'company_profile.html', context)



from django.shortcuts import render

# ... (other views)

def jobrecruiter(request):
    # Retrieve job openings for recruiters
    companies = Company.objects.all()  # You might need to adjust this query as needed
    context = {'companies': companies}
    return render(request, 'jobrecruiter.html', context)


def jobseeker(request):
    # Redirect or render the appropriate jobseeker page
    # Assuming you have a separate page for jobseekers similar to jobrecruiter
    # You might retrieve job openings for job seekers here if needed
    return render(request, 'jobseeker.html')  # You can adjust the context if needed
