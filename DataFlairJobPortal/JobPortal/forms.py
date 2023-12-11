from django import forms
from .models import JobSeeker, Recruiter, Company

class JobSeekerForm(forms.ModelForm):  # Modified from CandidateForm to JobSeekerForm
    class Meta:
        model = JobSeeker  # Changed model from Candidate to JobSeeker
        fields = '__all__'

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
