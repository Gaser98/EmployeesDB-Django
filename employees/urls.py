from django.urls import path
from employees.views import *

urlpatterns = [
    path('index', index, name='employees.index'),    
]



