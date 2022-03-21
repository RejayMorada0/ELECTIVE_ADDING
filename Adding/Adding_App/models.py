from django.db import models
import datetime
import os

# Create your models here.


#All Subjects
class All_Subject(models.Model):
    sub_code = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)
    year_and_sem = models.CharField(max_length=100)
    offer_stats = models.CharField(max_length=100)