from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('jobseeker/register/', views.jobseeker_register, name='jobseeker_register'),
    path('jobseeker/login/', views.jobseeker_login, name='jobseeker_login'),
    path('recruiter/register/', views.recruiter_register, name='recruiter_register'),
     path('recruiter/profile/', views.recruiter_profile, name='recruiter_profile'),
    path('jobseeker/profile/', views.jobseeker_profile, name='jobseeker_profile'),
    path('company/profile/', views.company_profile, name='company_profile'),
    path('company/update/', views.company_update, name='company_update'),
     path('recruiter/update/', views.recruiter_update, name='recruiter_update'),
    path('jobseeker/update/', views.jobseeker_update, name='jobseeker_update'),
    path('jobseeker/jobs/', views.jobseeker_jobs, name='jobseeker'),
    path('apply/', views.apply, name='apply'),
    path('recruiters/', views.recruiters, name='recruiters'),
    path('resumescreening/', views.resumescreening, name='resumescreening'),
    path('logout/', views.user_logout, name='logout'),
    # Add other paths as needed for different views or functionalities
]
