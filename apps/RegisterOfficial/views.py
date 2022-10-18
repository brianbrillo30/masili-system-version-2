from django.shortcuts import render

# Create your views here.

def add_official_account(request):
    return render (request, 'RegisterOfficial/register_official.html')
