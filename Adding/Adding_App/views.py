from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from pyexpat.errors import messages
#from django.contrib import messages

from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration, ReceiverRegistration

import mysql.connector as sql


# Create your views here.
installed_apps = ['Adding_App']


#Login Page
def index(request):
   return render(request, 'Adding_App/index.html')

#Sign Up
def registration(request):
    form = StudentRegistration()
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('index')
    context =  {'form': form }
    return render(request, 'Adding_App/registration.html', context)


#Head
def head(request):
    data = all_subjects.objects.all()
    context={
    'data': data
    }
    return render(request, 'Adding_App/head.html',context)

    # form = ReceiverRegistration()
    # if request.method == "POST":
    #     form ReceiverRegistration (request. POST)
    #     if form.is_valid ():
    #         form.save ()
    #         return redirect('index')
    # context = { 'form': form }
    # return render(request, 'Adding_App/head.html.html', context)

    

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
    return render(request, 'Adding_App/pic.html')

def checking(request):
    return render(request, 'Adding_App/checking.html')

def studentrecords(request):
    return render(request, 'Adding_App/studentrecords.html')

#student
def student(request):
    return render(request, 'Adding_App/student.html')
