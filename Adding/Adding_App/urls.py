from django.urls import path
from . import views

app_name = 'Adding_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]