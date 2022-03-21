from django.shortcuts import redirect, render
#from django.http import HttpResponse

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
