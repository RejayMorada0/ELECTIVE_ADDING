from os import name
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Adding_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('registration/', views.userregistration, name='registration'),
    path('logout/', views.logoutUser, name= 'logout'),
    #head
    path('head/', views.head, name='head'),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('addAction', views.addAction, name='addAction'),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('destroy/<int:id>', views.destroy),
    path('requestapproval/', views.requestapproval, name='requestapproval'),
    #pic
    path('pic/', views.pic, name='pic'),
    path('checking/', views.checking, name='checking'),
    path('studentrecords/', views.studentrecords, name='studentrecords'),
    #student
    path('student/', views.student, name='student'),
]

    
