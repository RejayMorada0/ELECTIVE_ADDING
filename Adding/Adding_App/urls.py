from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'Adding_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('Register/', views.register, name='register'),
    path('homepage/', views.login, name='login'),
    #path('logout/',),
    #head
    path('head/', views.head, name='head'),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('requestapproval/', views.requestapproval, name='requestapproval'),
    #pic
    path('pic/', views.pic, name='pic'),
    path('checking/', views.checking, name='checking'),
    path('studentrecords/', views.studentrecords, name='studentrecords'),
    #student
    path('student/', views.student, name='student'),
]