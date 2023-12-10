from django import forms
from .models import Recruiter, JobSeeker, Company

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'  # Include all fields from the model

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = '__all__'  # Include all fields from the model

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'  # Include all fields from the model
