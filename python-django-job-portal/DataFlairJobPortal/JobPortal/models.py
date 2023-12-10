from django.db import models

class Recruiter(models.Model):
    username = models.CharField(max_length=50, help_text='Enter a unique username')
    password = models.CharField(max_length=50)
    email = models.EmailField(help_text='Enter a valid email address')
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    qualifications = models.TextField()
    role = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    strengths = models.TextField()
    nationality = models.CharField(max_length=50)

class JobSeeker(models.Model):
    username = models.CharField(max_length=50, help_text='Enter a unique username')
    password = models.CharField(max_length=50)
    email = models.EmailField(help_text='Enter a valid email address')
    full_name = models.CharField(max_length=100)
    application_id = models.CharField(max_length=20)
    qualifications = models.TextField()
    role = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    nationality = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/', help_text='Upload resume') 

class Company(models.Model):
    admin = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='Enter company name')
    company_type = models.CharField(max_length=100)
    employees = models.PositiveIntegerField(default=0)
    vacancies = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    # Other fields related to company details.
