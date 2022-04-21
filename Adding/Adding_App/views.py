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
        data.image = request.FILES["file"]
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
    if request.method =='POST':
        data1 = all_subjects.objects.get(id=id)
        data1.sub_code = request.POST.get('sub_code')
        data1.sub_name = request.POST.get('sub_name')
        data1.year = request.POST.get('year')
        data1.semester = request.POST.get('semester')
        data1.offer_stats = request.POST.get('offer_stats')
        data1.save()
        return redirect('/head') 
    return render(request, 'Adding_App/edit.html', {'data':data})

def delete(request,id):
    data = all_subjects.objects.get(id=id)
    data.delete()
    return redirect("/head/")
    
#pic
def pic(request):
    students = registration.objects.all()
    context={'students': students}
    print(context)
    return render(request, 'Adding_App/pic.html', context)


def checking(request,id):
    data = registration.objects.get(id=id)
    image = registration.objects.filter(username=data)
    studentReq = student_request.objects.filter(stud_id=data.id)
    offerSub = all_subjects.objects.filter(offer_stats='Offer')
    subject = all_subjects.objects.all()
    ids = registration.objects.filter(id=id)
    return render(request, 'Adding_App/checking.html',  {'subject':subject, 'ids':ids, 'data':data, 'image':image, 'studentReq':studentReq , 'offerSub':offerSub } )


def addRemark(request,id):
    data = registration.objects.get(id=id)
    if request.method =='POST':
        stud_id_id = request.POST.get('stud_id_id')
        sub_code_id = request.POST.get('sub_code_id')
        grades = request.POST.get('grades')
        remarks = request.POST.get('remarks')
        subject = all_subjects.objects.get(id=sub_code_id)
        data = student_request.objects.create(stud_id_id = stud_id_id, sub_code_id = sub_code_id, subject = subject.sub_code, grades = grades, remarks = remarks)
        data.save()
        return redirect('/checking/'+ str(id))
   
def editRemark(request, id):
    ids = registration.objects.filter(id=id)
    data= student_request.objects.filter(stud_id=id)
    print(ids)
    fil_data = registration.objects.filter(id=id)
    print(fil_data)
    if request.method =='POST':
        sub_code_id = request.POST.get('sub_code_id')
        data2= student_request.objects.get(sub_code_id=sub_code_id, stud_id=id)
        print(data2)
        data2.stud_id_id = request.POST.get('stud_id_id')
        data2.sub_code_id = request.POST.get('sub_code_id')
        data2.grades = request.POST.get('grades')
        data2.remarks = request.POST.get('remarks')
        data2.save()
        return redirect('/checking/'+ str(id))
    return render(request, 'Adding_App/editRemark.html', {'data':data, 'ids':ids, 'fil_data':fil_data})


def deleteRemark(request,id):
    data= student_request.objects.filter(stud_id=id)
    print(data)
    data.delete()
    return redirect('/checking/'+ str(id))
   

def studentrecords(request):
    return render(request, 'Adding_App/studentrecords.html')


