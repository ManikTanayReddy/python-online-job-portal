from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Enter company name')
    company_type = models.CharField(max_length=100)
    employees = models.PositiveIntegerField(default=0)
    vacancies = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    main_branch_city = models.CharField(max_length=100, help_text='Enter main branch city')

    def __str__(self):
        return self.name

class JobSeeker(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True, upload_to='resumes/')
    companies = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return self.name

class Recruiter(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20)
    qualifications = models.TextField()
    role = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    strengths = models.TextField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
