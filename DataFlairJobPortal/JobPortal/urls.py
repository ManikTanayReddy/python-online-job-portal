from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    # URL for the index page
    path('index/', views.index, name='index'),
    # URLs for job seekers
    path('jobseeker/register/', views.jobseeker_register, name='jobseeker_register'),
    path('jobseeker/login/', views.jobseeker_login, name='jobseeker_login'),
    path('jobseeker/logout/', views.jobseeker_logout, name='jobseeker_logout'),
    # URLs for recruiters
    path('recruiter/register/', views.recruiter_register, name='recruiter_register'),
    path('recruiter/login/', views.recruiter_login, name='recruiter_login'),
    path('recruiter/logout/', views.recruiter_logout, name='recruiter_logout'),
    
    
    path('candidate_profile/', views.candidateProfile, name='candidate_profile'),
    path('recruiter_profile/', views.recruiterProfile, name='recruiter_profile'),
    path('company_profile/', views.companyProfile, name='company_profile'),
    path('jobrecruiter/', views.jobrecruiter, name='jobrecruiter'),
    path('jobseeker/', views.jobseeker, name='jobseeker'),
    # Other URLs for your application...
]

