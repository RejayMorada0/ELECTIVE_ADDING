from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model
import os

# Create your models here.

#All Subjects
class all_subjects(models.Model):
    sub_code = models.CharField(max_length=100, unique=True)
    sub_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    offer_stats = models.CharField(max_length=100)



#Student Accounts
class student_accounts(models.Model):
    stud_id = models.CharField(max_length=100,editable=False, unique=True)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    passw = models.CharField(max_length=100)
    stud_stats = models.CharField(max_length=100)
    image = models.ImageField(max_length=100)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email


    #Function para may TUPC sa unahan 
    #https://stackoverflow.com/questions/52070462/django-generate-custom-id
    
    

#Student Request
#foreign key (https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/)
#https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name
#https://stackoverflow.com/questions/2606194/django-error-message-add-a-related-name-argument-to-the-definition
class student_request(models.Model): 
    stud_id = models.ForeignKey(student_accounts, on_delete=models.CASCADE, related_name='+')
    sub_code = models.ForeignKey(all_subjects, on_delete=models.CASCADE, related_name='+')
    sub_name = models.ForeignKey(all_subjects, on_delete=models.CASCADE, related_name='+')
    year = models.ForeignKey(all_subjects, on_delete=models.CASCADE, related_name='+')
    semester = models.ForeignKey(all_subjects, on_delete=models.CASCADE, related_name='+')
    remarks = models.CharField(max_length=100)



#Head and PIC
class administrator_access(models.Model): #add user type (head or pic) one table
    email = models.EmailField(max_length=100, unique=True)
    passw = models.CharField(max_length=100)

#users model
#https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
# class User(AbstractUser):
#   USER_TYPE_CHOICES = (
#       (1, 'student'),
#       (2, 'pic'),
#       (3, 'head'),
#   )

#   user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)