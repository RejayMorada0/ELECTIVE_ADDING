from django.shortcuts import redirect, render
from django.http import HttpResponse
#from all_subjects.models import all_subjects

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


#Add Subject
def add_sub(request):
    if request.method=='POST':
        sub_code = request.POST.get('sub_code')
        sub_name = request.POST.get('sub_name')
        yr_and_sem = request.POST.get('yr_and_sem')
        offer_stats = request.POST.get('offer_stats')

        data = all_subjects.objects.create(sub_code = sub_code, sub_name = sub_name, yr_and_sem = yr_and_sem, offer_stats = offer_stats)
        data.save()
        return render(request, 'Adding_App/head.html')





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
