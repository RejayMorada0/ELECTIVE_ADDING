from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
#from pyexpat.errors import messages
from django.contrib import messages

from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration, ReceiverRegistration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.db.models import Q

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
@login_required(login_url='/index')
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
@login_required(login_url='/index')
def head(request):
    data = all_subjects.objects.all()
    context={
    'data': data
    }
    print(context)
    return render(request, 'Adding_App/head.html',context)


@login_required(login_url='/index')
def requestapproval(request):
    q = Q(stud_stats='Waiting For Approval') | Q(stud_stats='Approved')
    students = registration.objects.filter(q)
    context={'students': students}
    return render(request, 'Adding_App/requestapproval.html', context)

@login_required(login_url='/index')
def checking1(request,id):
    data = registration.objects.get(id=id)
    image = registration.objects.filter(username=data)
    studentReq = student_request.objects.filter(stud_id=data.id)
    offerSub = all_subjects.objects.filter(offer_stats='Offer')
    subject = all_subjects.objects.all()
    ids = registration.objects.filter(id=id)
    stud_stats = data.stud_stats
    print(stud_stats)
    return render(request, 'Adding_App/checking1.html',  { 'subject':subject, 'ids':ids, 'data':data, 'image':image, 'studentReq':studentReq , 'offerSub':offerSub, 'stud_stats':stud_stats } )

@login_required(login_url='/index')
def adminApprove(request):
    stud_id = request.POST.get('stud_id')
    print(stud_id)
    ids = registration.objects.get(stud_id=stud_id)
    ids.stud_stats = 'Approved'
    ids.save()
    print(ids)
    return redirect('/requestapproval/')    

#Add Subject
@login_required(login_url='/index')
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


@login_required(login_url='/index')
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
@login_required(login_url='/index')
def pic(request):
    # q = Q(stud_stats='Processing') | Q(stud_stats='Requested')
    students = registration.objects.filter(stud_stats='Requested')
    return render(request, 'Adding_App/pic.html', {'students': students})


@login_required(login_url='/index')
def checking(request,id):
    data = registration.objects.get(id=id)
    image = registration.objects.filter(username=data)
    studentReq = student_request.objects.filter(stud_id=data.id)
    offerSub = all_subjects.objects.filter(offer_stats='Offer')
    subject = all_subjects.objects.all()
    ids = registration.objects.filter(id=id)
    stud_stats = data.stud_stats
    print(stud_stats)
    return render(request, 'Adding_App/checking.html',  { 'subject':subject, 'ids':ids, 'data':data, 'image':image, 'studentReq':studentReq , 'offerSub':offerSub, 'stud_stats':stud_stats } )


@login_required(login_url='/index')
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

@login_required(login_url='/index')   
def editRemark(request, id):
    ids = registration.objects.filter(id=id)
    data= student_request.objects.filter(stud_id=id)
    print(ids)
    fil_data = registration.objects.filter(id=id)
    print(fil_data)
    if request.method =='POST':
        sub_code_id = request.POST.get('sub_code_id')
        data1= student_request.objects.get(sub_code_id=sub_code_id, stud_id=id)
        print(data1)
        data1.stud_id_id = request.POST.get('stud_id_id')
        data1.sub_code_id = request.POST.get('sub_code_id')
        data1.grades = request.POST.get('grades')
        data1.remarks = request.POST.get('remarks')
        data1.save()
        return redirect('/checking/'+ str(id))
    return render(request, 'Adding_App/editRemark.html', {'data':data, 'ids':ids, 'fil_data':fil_data})


def deleteRemark(request,id):
    data= student_request.objects.filter(stud_id=id)
    print(data)
    data.delete()
    return redirect('/checking/'+ str(id))

def picRequest(request):
    stud_id = request.POST.get('stud_id')
    print(stud_id)
    ids = registration.objects.get(stud_id=stud_id)
    ids.stud_stats = 'Waiting For Approval'
    ids.save()
    print(ids)
    return redirect('/studentrecords/')

@login_required(login_url='/index')
def studentrecords(request):
    q = Q(stud_stats='Waiting For Approval') | Q(stud_stats='Approved')
    students = registration.objects.filter(q)
    # students = registration.objects.filter(stud_stats='Processing''Requested')
    context={'students': students}
    print(context)
    return render(request, 'Adding_App/studentrecords.html', context)



