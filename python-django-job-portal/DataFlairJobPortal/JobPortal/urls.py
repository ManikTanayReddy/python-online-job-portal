from django.urls import path
from . import views

urlpatterns = [
    # URLs for Registrations
    path('recruiter/registration/', views.recruiter_registration, name='recruiter_registration'),
    path('jobseeker/registration/', views.job_seeker_registration, name='job_seeker_registration'),

    # Login/Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Job Listings
    path('job/listing/', views.job_listing, name='job_listing'),

    # Company Profile
    path('company/profile/', views.company_profile, name='company_profile'),

    # Home/Index
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),

    # Job Application
    path('apply/', views.apply_for_job, name='apply'),

    # Review Applicants
    path('review/', views.review_applicants, name='review'),

    # Recruiter URLs
    path('recruiter/dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('recruiter/create/', views.create_company_profile, name='create_company_profile'),
    path('recruiter/update/', views.update_company_profile, name='update_company_profile'),

    # Add other URLs as needed...
]
from django.urls import path
from . import views

urlpatterns = [
    # URLs for Registrations
    path('recruiter/registration/', views.recruiter_registration, name='recruiter_registration'),
    path('jobseeker/registration/', views.job_seeker_registration, name='job_seeker_registration'),

    # Login/Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Job Listings
    path('job/listing/', views.job_listing, name='job_listing'),

    # Company Profile
    path('company/profile/', views.company_profile, name='company_profile'),

    # Home/Index
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),

    # Job Application
    path('apply/', views.apply_for_job, name='apply'),

    # Review Applicants
    path('review/', views.review_applicants, name='review'),

    # Recruiter URLs
    path('recruiter/dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('recruiter/create/', views.create_company_profile, name='create_company_profile'),
    path('recruiter/update/', views.update_company_profile, name='update_company_profile'),

    # Add other URLs as needed...
]
