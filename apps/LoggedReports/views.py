from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.



def loggedReports(request):
    return render(request, 'LoggedReports/logged_reports.html')