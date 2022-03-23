from django.contrib import admin
from .models import all_subjects, student_accounts, student_request, head_access

# Register your models here.

admin.site.register(all_subjects)
admin.site.register(student_accounts)
