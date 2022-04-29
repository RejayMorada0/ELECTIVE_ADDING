from django.http import HttpResponse, HttpResponseRedirect, FileResponse
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

import io
from reportlab.pdfgen import canvas


# Create your views here.
installed_apps = ['Adding_App']


#LOGIN PAGE
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

#SIGN UP PAGE
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

#STUDENT USER INTERFACE
@login_required(login_url='/index')
def student(request):
    if request.user.is_authenticated and request.user.userType == 'STDNT':
        data = registration.objects.filter(id = request.user.pk)
        current_user = request.user
        username = current_user.username
        stud_stats = current_user.stud_stats
        context = { 'data': data, 'stud_stats': stud_stats }
        print(context)
        if request.method == 'POST':
            data = registration.objects.get(username=username)
            data.image = request.FILES["image"]
            data.stud_stats = 'Requested'
            data.save()
            return redirect('/student') 
        return render(request, 'Adding_App/student.html',context)
    return redirect('/index')

def studentRequestNew(request):
    if request.method == 'POST':
        stud_id = request.POST.get('stud_id')
        data = registration.objects.get(stud_id=stud_id)
        data.stud_stats = 'Processing'
        data.image = ''
        data.save()
        return redirect('/student')

def exportPDF(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Student Request.pdf')  

#HEAD USER INTERFACE
@login_required(login_url='/index')
def head(request):
    if request.user.is_authenticated and request.user.userType == 'DH':
        data = all_subjects.objects.all()
        context={
        'data': data
        }
        print(context)
        return render(request, 'Adding_App/head.html',context)
    return redirect('/index')


@login_required(login_url='/index')
def requestapproval(request):
    if request.user.is_authenticated and request.user.userType == 'DH':
        q = Q(stud_stats='Waiting For Approval') | Q(stud_stats='Approved')
        students = registration.objects.filter(q)
        context={'students': students}
        return render(request, 'Adding_App/requestapproval.html', context)
    return redirect('/index')


@login_required(login_url='/index')
def checking1(request,id):
    if request.user.is_authenticated and request.user.userType == 'DH':
        data = registration.objects.get(id=id)
        image = registration.objects.filter(username=data)
        studentReq = student_request.objects.filter(stud_id=data.id)
        offerSub = all_subjects.objects.filter(offer_stats='Offer')
        subject = all_subjects.objects.all()
        ids = registration.objects.filter(id=id)
        stud_stats = data.stud_stats
        print(stud_stats)
        return render(request, 'Adding_App/checking1.html',  { 'subject':subject, 'ids':ids, 'data':data, 'image':image, 'studentReq':studentReq , 'offerSub':offerSub, 'stud_stats':stud_stats } )
    return redirect('/index')


def adminApprove(request):
    stud_id = request.POST.get('stud_id')
    print(stud_id)
    ids = registration.objects.get(stud_id=stud_id)
    ids.stud_stats = 'Approved'
    ids.save()
    print(ids)
    return redirect('/requestapproval/')    

#Add Subject
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
    if request.user.is_authenticated and request.user.userType == 'DH':
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
    return redirect('/index')


def delete(request,id):
    data = all_subjects.objects.get(id=id)
    data.delete()
    return redirect('/head')
    
#PIC USER INTERFACE
@login_required(login_url='/index')
def pic(request):
    if request.user.is_authenticated and request.user.userType == 'PIC':
        students = registration.objects.filter(stud_stats='Requested')
        return render(request, 'Adding_App/pic.html', {'students': students})
    return redirect('/index')


@login_required(login_url='/index')
def checking(request,id):
    if request.user.is_authenticated and request.user.userType == 'PIC':
        data = registration.objects.get(id=id)
        image = registration.objects.filter(username=data)
        studentReq = student_request.objects.filter(stud_id_id=data.id)
        print(studentReq,'hello')
        offerSub = all_subjects.objects.filter(offer_stats='Offer')
        subject = all_subjects.objects.all()
        ids = registration.objects.filter(id=id)
        stud_stats = data.stud_stats
        print(stud_stats)
        return render(request, 'Adding_App/checking.html',  { 'subject':subject, 'ids':ids, 'data':data, 'image':image, 'studentReq':studentReq , 'offerSub':offerSub, 'stud_stats':stud_stats } )
    return redirect('/index')


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
    if request.user.is_authenticated and request.user.userType == 'PIC':
        data= student_request.objects.filter(id=id)
        if request.method =='POST':
            stud_id_id = request.POST.get('stud_id_id')
            data1= student_request.objects.get(id=id)
            print(data1, "hello")
            data1.id = request.POST.get('id')
            data1.stud_id_id = request.POST.get('stud_id_id')
            data1.sub_code_id = request.POST.get('sub_code_id')
            data1.grades = request.POST.get('grades')
            data1.remarks = request.POST.get('remarks')
            data1.save()
            return redirect('/checking/'+ str(stud_id_id))
        return render(request, 'Adding_App/editRemark.html', {'data':data} )
    return redirect('/index')

def deleteRemark(request,id):
    data= student_request.objects.get(id=id)
    print(data)
    print(data.stud_id_id)
    data.delete()
    return redirect('/checking/'+ str(data.stud_id_id))

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
    if request.user.is_authenticated and request.user.userType == 'PIC':
        q = Q(stud_stats='Waiting For Approval') | Q(stud_stats='Approved')
        students = registration.objects.filter(q)
        context={'students': students}
        print(context)
        return render(request, 'Adding_App/studentrecords.html', context)
    return redirect('/index')



