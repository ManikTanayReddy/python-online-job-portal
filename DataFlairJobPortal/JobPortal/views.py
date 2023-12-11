from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import JobSeekerForm, RecruiterForm
from .models import Recruiter, JobSeeker, Company
from .forms import CompanyForm 

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

def recruiter_profile(request):
    recruiter = Recruiter.objects.get(user=request.user)
    return render(request, 'recruiter_profile.html', {'recruiter': recruiter})

def jobseeker_profile(request):
    jobseeker = JobSeeker.objects.get(user=request.user)
    return render(request, 'jobseeker_profile.html', {'jobseeker': jobseeker})


 # Assuming you have created the form

def company_profile(request):
    # Fetch company profile based on the logged-in user
    admin = request.user.recruiter
    company = Company.objects.get(admin=admin)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_profile')
    else:
        form = CompanyForm(instance=company)
    
    context = {
        'form': form,
        'company': company,
    }
    return render(request, 'company_profile.html', context)

def company_update(request):
    # Fetch company profile based on the logged-in user
    admin = request.user.recruiter
    company = Company.objects.get(admin=admin)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_profile')
    else:
        form = CompanyForm(instance=company)
    
    context = {
        'form': form,
        'company': company,
    }
    return render(request, 'company_update.html', context)

def recruiter_update(request):
    user = request.user
    if request.method == 'POST':
        recruiter = Recruiter.objects.get(user=user)
        form = RecruiterForm(request.POST, instance=recruiter)
        if form.is_valid():
            form.save()
            return redirect('recruiter_profile')  # Redirect to recruiter profile after update
    else:
        recruiter = Recruiter.objects.get(user=user)
        form = RecruiterForm(instance=recruiter)
    return render(request, 'recruiter_update.html', {'form': form})

def jobseeker_update(request):
    user = request.user
    if request.method == 'POST':
        jobseeker = JobSeeker.objects.get(user=user)
        form = JobSeekerForm(request.POST, instance=jobseeker)
        if form.is_valid():
            form.save()
            return redirect('jobseeker_profile')  # Redirect to jobseeker profile after update
    else:
        jobseeker = JobSeeker.objects.get(user=user)
        form = JobSeekerForm(instance=jobseeker)
    return render(request, 'jobseeker_update.html', {'form': form})

def jobseeker_jobs(request):
    # Fetch companies from the database
    companies = Company.objects.all()  # Assuming Company is your model name
    context = {'companies': companies}
    return render(request, 'jobseeker.html', context)

def apply(request):
    return render(request, 'apply.html')

def recruiters(request):
    # Your logic to fetch applied jobseekers and render recruiter.html
    candidates = JobSeeker.objects.all()  # Query to fetch jobseekers
    return render(request, 'recruiter.html', {'candidates': candidates})

def resumescreening(request):
    return render(request, 'resumescreening.html')

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout
