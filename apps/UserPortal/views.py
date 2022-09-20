from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "UsersideTemplate/index.html")

def about(request):
    return render(request, "UsersideTemplate/about.html")

<<<<<<< HEAD
def ServicesPortal(request):
    return render(request, "UsersideTemplate/service_portal.html")
=======
def userLogin(request):
    return render(request, "UsersideTemplate/login.html")
>>>>>>> db5d86e741def260a7d50c5e769f70868fc79309
