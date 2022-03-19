from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

#def index (request):
#    return HttpResponse( "Welcome to Web Development 2")

def index(request):#login student
    return render(request, 'Adding_Of_Sub/index.html')