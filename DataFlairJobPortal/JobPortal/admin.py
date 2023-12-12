from django.contrib import admin
from .models import Company, JobSeeker, Recruiter

# Register your models here.
admin.site.register(Company)
admin.site.register(JobSeeker)
admin.site.register(Recruiter)

