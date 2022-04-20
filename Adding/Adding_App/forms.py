from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import registration, student_request

class StudentRegistration(UserCreationForm):
    class Meta:
        model = registration
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'section', 'stud_id']


class ReceiverRegistration(UserCreationForm):
    class Meta:
        model = registration
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'section','stud_id', 'stud_stats', 'image', 'userType']


