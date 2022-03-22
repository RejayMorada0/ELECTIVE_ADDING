from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'Adding_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    #head
    path('head/', views.head, name='head'),
    path('requestapproval/', views.requestapproval, name='requestapproval'),
    path('Add_Remove_Sub/', views.addAction, name='addAction'),
    path('Add_Remove_Sub/', views.removeAction, name='removeAction'),
    path('showAllSub/', views.showAllSub, name='showAllSub'),
    #pic
    path('pic/', views.pic, name='pic'),
    path('checking/', views.checking, name='checking'),
    path('studentrecords/', views.studentrecords, name='studentrecords'),
    #student
    path('student/', views.student, name='student'),
]