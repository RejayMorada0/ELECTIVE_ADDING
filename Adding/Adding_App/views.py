from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import all_subjects, student_accounts, head_access
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

def register(request):
    if request.method == 'POST':
        stud_id = request.POST.get('stud_id')
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        section = request.POST.get('section')
        email = request.POST.get('email')
        passw = request.POST.get('passw')
        cpassw = request.POST.get('cpassw')
        data = student_accounts.objects.create(stud_id=stud_id, fn=fn, ln=ln, section=section, email=email, passw=passw)
        data.save()
        return render(request, 'Adding_App/index.html')

def login(request):
    if request.method=="POST":
        conn = sql.connect(host = "localhost", user = "root", password = "", database = 'adding_subjects_db')
        cursor = conn.cursor()
        req = request.POST
        for key, value in req.items():
            if key == "email":
                email = value
            if key == "passw":
                passw = value
        
        select = "SELECT * FROM adding_app_student_accounts WHERE email='{}' and passw='{}'".format(email,passw)
        
        cursor.execute(select)
        student = tuple(cursor.fetchall())
        if student != ():
            data = student_accounts.objects.filter(email = email)
            #return render(request, 'Adding_App/student.html', {'data':data})
            return redirect('/student', {'data':data})
        else:
            conn = sql.connect(host = "localhost", user = "root", password = "", database = 'adding_subjects_db')
            cursor = conn.cursor()
            req = request.POST
            for key, value in req.items():
                if key == "email":
                    email = value
                if key == "passw":
                    passw = value
            
            select = "SELECT * FROM adding_app_head_access WHERE email1='{}' and passw1='{}'".format(email,passw)
            cursor.execute(select)
            head = tuple(cursor.fetchall())
            if head != ():
                data = head_access.objects.filter(email1 = email)
                #return render(request, 'Adding_App/head.html', {'data':data})
                return redirect('/head', {'data':data})
            else:
                return redirect('/index')       

    return render(request, 'Adding_App/index.html') 

#Head
def head(request):
    data = all_subjects.objects.all()
    context={
    'data': data
    }
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
