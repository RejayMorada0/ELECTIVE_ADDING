from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
#from pyexpat.errors import messages
from django.contrib import messages

from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration, ReceiverRegistration
from django.contrib.auth import authenticate, login, logout

import mysql.connector as sql


# Create your views here.
installed_apps = ['Adding_App']


#Login Page
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        print(user)

        if user is not None and user.userType == 'STDNT':
            login(request, user)
            return redirect('/student')
        
        elif user is not None and user.userType == 'DH':
            login(request, user)
            return redirect('/head')

        elif user is not None and user.userType == 'PIC':
            login(request, user)
            return redirect('/pic')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'Adding_App/index.html')

#Sign Up
def userregistration(request):
    form = StudentRegistration()
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/index')
    context =  {'form': form }
    return render(request, 'Adding_App/registration.html', context)

#Log Out
def logoutUser(request):
    logout(request)
    return redirect('/index')

#student
def student(request):
    data = registration.objects.filter(id = request.user.pk)
    
    current_user = request.user
    username = current_user.username
    stud_stats = current_user.stud_stats
    context = { 'data': data, 'stud_stats': stud_stats }
    print(context)
    if request.method == 'POST':
        data = registration.objects.get(username=username)
        data.image = request.POST.get('image')
        data.stud_stats = 'Requested'
        data.save()
        return redirect('/student') 
    return render(request, 'Adding_App/student.html',context)

#Head
def head(request):
    data = all_subjects.objects.all()
    context={
    'data': data
    }
    print(context)
    return render(request, 'Adding_App/head.html',context)
  

def requestapproval(request):
    return render(request, 'Adding_App/requestapproval.html')

#Add Subject
def addsubject(request):
    return render(request, 'Adding_App/addsubject.html')

def addAction(request):
    if request.method=='POST':
        sub_code = request.POST.get('sub_code')
        sub_name = request.POST.get('sub_name')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        offer_stats = request.POST.get('offer_stats')

        data = all_subjects.objects.create(sub_code = sub_code, sub_name = sub_name, year = year, semester = semester, offer_stats = offer_stats)
        data.save()
        return redirect('/head')

def edit(request,id):
    data = all_subjects.objects.get(id=id)
    return render(request, 'Adding_App/edit.html', {'data':data})

def delete(request,id):
    data = all_subjects.objects.get(id=id)
    return render(request, 'Adding_App/delete.html', {'data':data})

def destroy(request,id):
    data = all_subjects.objects.get(id=id)
    data.delete()
    return redirect("/head/")
    
def update(request,id):
    data = all_subjects.objects.get(id=id)
    data.sub_code = request.POST.get('sub_code')
    data.sub_name = request.POST.get('sub_name')
    data.year = request.POST.get('year')
    data.semester = request.POST.get('semester')
    data.offer_stats = request.POST.get('offer_stats')
    data.save()
    return redirect('/head') 


#pic
def pic(request):
    data = registration.objects.filter(userType='STDNT')
    context = {'data': data}
    print(context)
    if request.method == 'POST':
        internal_id = request.POST.get('internal_id')
        instance = registration.objects.get(stud_id=internal_id)
        print(internal_id)
        studentrequest = student_request.objects.filter(stud_id = internal_id)
        context1 = {'studentrequest':studentrequest, 'internal_id': internal_id}
        return render(request, 'Adding_App/checking.html', context1)
    return render(request, 'Adding_App/pic.html', context)

def checking(request):
    data = all_subjects.objects.filter(offer_stats = 'Offer')
    context = {'data': data}
    print(context)
    return render(request, 'Adding_App/checking.html', context)

def addRemark(request):
    if request.method=='POST':
        sub_code = request.POST.get('sub_code')
        sub_name = request.POST.get('sub_name')

def studentrecords(request):
    return render(request, 'Adding_App/studentrecords.html')


