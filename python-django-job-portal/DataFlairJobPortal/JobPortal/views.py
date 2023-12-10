from django.shortcuts import render, redirect
from .forms import RecruiterForm, JobSeekerForm
from .models import Recruiter, JobSeeker

def recruiter_registration(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page upon successful registration
    else:
        form = RecruiterForm()
    return render(request, 'recruiter_registration.html', {'form': form})

def job_seeker_registration(request):
    if request.method == 'POST':
        form = JobSeekerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page upon successful registration
    else:
        form = JobSeekerForm()
    return render(request, 'job_seeker_registration.html', {'form': form})

# Other views for login, dashboard, profile, job listing, etc. go here

from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company

def company_profile(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page upon successful profile update
    else:
        # Fetch the existing company profile (assuming there's only one profile)
        company = Company.objects.first()  # You can update this logic based on your requirements
        form = CompanyForm(instance=company)
    return render(request, 'company_profile.html', {'form': form})


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def job_seeker_registration(request):
    # Implement job seeker registration logic
    return render(request, 'job_seeker_registration.html')

def recruiter_registration(request):
    # Implement recruiter registration logic
    return render(request, 'recruiter_registration.html')

#Update views.py for Login:

def login_view(request):
    # Implement login logic
    return render(request, 'login.html')

#Update views.py for Dashboard:
def dashboard(request):
    # Implement dashboard logic
    return render(request, 'dashboard.html')

#Job Listings View and Template
def job_listing(request):
    # Implement job listing logic
    return render(request, 'job_listing.html')

#Company Profile View and Template
def company_profile(request):
    # Implement company profile logic
    return render(request, 'company_profile.html')

def apply_for_job(request):
    if request.method == 'POST':
        # Implement job application logic
        return redirect('waitinglist')  # Redirect to the waiting list page after applying
    else:
        # Pass applicants' details to the template for initial view/rendering
        return render(request, 'apply.html')


def review_applicants(request):
    return render(request, 'review.html')


from django.shortcuts import render, redirect
from .models import Company  # Import your Company model

def recruiter_dashboard(request):
    recruiter = request.user  # Assuming the logged-in user is the recruiter
    company = Company.objects.filter(admin=recruiter).first()
    return render(request, 'recruiter_dashboard.html', {'company': company})

def create_company_profile(request):
    if request.method == 'POST':
        recruiter = request.user
        name = request.POST.get('name')
        # Retrieve other form fields similarly
        Company.objects.create(admin=recruiter, name=name)
        # Create the company profile
        return redirect('recruiter_dashboard')

    return render(request, 'recruiter_dashboard.html')

def update_company_profile(request):
    recruiter = request.user
    company = Company.objects.filter(admin=recruiter).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        # Retrieve other form fields similarly
        company.name = name
        # Update other company profile fields accordingly
        company.save()
        # Update the company profile
        return redirect('recruiter_dashboard')

    return render(request, 'update_company_profile.html', {'company': company})
