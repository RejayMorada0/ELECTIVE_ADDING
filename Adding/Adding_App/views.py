from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import all_subjects

from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
import mysql.connector as sql


# Create your views here.
installed_apps = ['Adding_App']

#def index (request):
#    return HttpResponse( "Welcome to Web Development 2")

#Login Page
def index(request):
   return render(request, 'Adding_App/index.html')

#Sign Up
def signup(request):
    return render(request, 'Adding_App/signup.html')

#Head
def head(request):
    return render(request, 'Adding_App/head.html')

def requestapproval(request):
    return render(request, 'Adding_App/requestapproval.html')

#Show All Subjects in Table
def showAllSub(request):
    all_subs = all_subjects.objects.all()
    return render(request, 'Adding_App/head.html',{'all_subs':all_subs}) 

#Add Subject
def addAction(request):
    if request.method=='POST':
        sub_code = request.POST.get('sub_code')
        sub_name = request.POST.get('sub_name')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        #offer_stats = request.POST.get('offer_stats')

        data = all_subjects.objects.create(sub_code = sub_code, sub_name = sub_name, year = year, semester = semester, offer_stats = "Not Offer")
        data.save()
        return render(request, 'Adding_App/head.html')

#Remove Subject
def removeAction(request,id):
    subject = all_subjects.objects.get(id = id)
    subject.delete()
    return redirect('/head')








#pic
def pic(request):
    return render(request, 'Adding_App/pic.html')

def checking(request):
    return render(request, 'Adding_App/checking.html')

def studentrecords(request):
    return render(request, 'Adding_App/studentrecords.html')

#student
def student(request):
    return render(request, 'Adding_App/student.html')
