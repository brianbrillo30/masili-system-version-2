from django.shortcuts import render

# Create your views here.

def indigency_module(request):
    return render (request, 'IndigencyManagement/indigency_module.html')