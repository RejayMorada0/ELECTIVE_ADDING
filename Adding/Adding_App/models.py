from django.db import models
import datetime
import os

# Create your models here.

#All Subjects
class all_subjects(models.Model):
    sub_code = models.CharField(max_length=100)
    sub_name = models.CharField(max_length=100)
    yr_and_sem = models.CharField(max_length=100)
    offer_stats = models.CharField(max_length=100)



#Student Accounts
class student_accounts(models.Model):
    stud_id = models.CharField(max_length=100)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passw = models.CharField(max_length=100)
    stud_stats = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    

#Student Request
class student_request(models.Model):
    trans_id = models.PositiveIntegerField(max_length=100)
    stud_id = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=100)
    sub_name = models.CharField(max_length=100)
    yr_and_sem = models.CharField(max_length=100)
    grades = models.FloatField(max_length=100)
    remarks = models.CharField(max_length=100)


#Head Access
class head_access(models.Model):
    email = models.EmailField(max_length=100)
    passw = models.CharField(max_length=100)


#PIC Access
class pic_access(models.Model):
    email = models.EmailField(max_length=100)
    passw = models.CharField(max_length=100)