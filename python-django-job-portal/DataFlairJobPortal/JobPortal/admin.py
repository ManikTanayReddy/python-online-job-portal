from django.contrib import admin
from .models import Recruiter, JobSeeker, Company

# Register your models here.
admin.site.register(Recruiter)
admin.site.register(JobSeeker)
admin.site.register(Company)
