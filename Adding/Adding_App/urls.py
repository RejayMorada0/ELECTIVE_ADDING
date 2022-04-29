from os import name
from django.urls import path, re_path
from django.conf.urls import static
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
    path('addAction', views.addAction, name='addAction'),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('requestapproval/', views.requestapproval, name='requestapproval'),
    path('adminApprove/', views.adminApprove, name='adminApprove'),
    #pic
    path('pic/', views.pic, name='pic'),
    path('checking/<int:id>', views.checking),
    path('checking1/<int:id>', views.checking1),
    path('addRemark/<int:id>', views.addRemark),
    path('editRemark/<int:id>', views.editRemark),
    path('deleteRemark/<int:id>', views.deleteRemark),
    path('picRequest/', views.picRequest, name='picRequest'),
    path('studentrecords/', views.studentrecords, name='studentrecords'),
    #student
    path('student/', views.student, name='student'),
    path('studentRequestNew/', views.studentRequestNew, name='studentRequestNew'),
    path('exportPDF/', views.exportPDF, name='exportPDF'),
]

    
