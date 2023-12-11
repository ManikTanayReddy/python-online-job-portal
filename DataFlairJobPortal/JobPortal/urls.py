from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('jobseeker/register/', views.jobseeker_register, name='jobseeker_register'),
    path('jobseeker/login/', views.jobseeker_login, name='jobseeker_login'),
    path('jobseeker/logout/', views.jobseeker_logout, name='jobseeker_logout'),
    path('recruiter/register/', views.recruiter_register, name='recruiter_register'),
    path('recruiter/login/', views.recruiter_login, name='recruiter_login'),
    path('recruiter/logout/', views.recruiter_logout, name='recruiter_logout'),
    # Add other paths as needed for different views or functionalities
]
