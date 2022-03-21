from django.db import models
import datetime
import os

# Create your models here.

#All Subjects
class all_subjects(models.Model):
    sub_code = models.CharField(max_length=100, primary_key=True)
    sub_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(max_length=100)
    semester = models.PositiveIntegerField(max_length=100)
    offer_stats = models.CharField(max_length=100)



#Student Accounts
class student_accounts(models.Model):
    stud_id = models.CharField(max_length=100,editable=False, primary_key=True)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    passw = models.CharField(max_length=100)
    stud_stats = models.CharField(max_length=100)
    image = models.ImageField(max_length=100)

    #Function para may TUPC sa unahan 
    #https://stackoverflow.com/questions/52070462/django-generate-custom-id
    def save(self, **kwargs):
        if not self.id:
            max = student_accounts.objects.aggregate(id_max=Max('stud_id'))['id_max']
            self.stud_id = "{}{:05d}".format('TUPC', max if max is not None else 1)
        super().save(*kwargs)
    

#Student Request
#foreign key (https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/)
class student_request(models.Model): 
    trans_id = models.PositiveIntegerField(max_length=100, primary_key=True)
    stud_id = models.ForeignKey(student_accounts, on_delete=models.CASCADE)
    sub_code = models.ForeignKey(all_subjects, on_delete=models.CASCADE)
    sub_name = models.ForeignKey(all_subjects, on_delete=models.CASCADE)
    year = models.ForeignKey(all_subjects, on_delete=models.CASCADE)
    semester = models.ForeignKey(all_subjects, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100)


#Head and PIC
class head_access(models.Model): #add user type (admin or pic) one table
    email = models.EmailField(max_length=100)
    passw = models.CharField(max_length=100)

#users model
#https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'pic'),
      (3, 'head'),
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)