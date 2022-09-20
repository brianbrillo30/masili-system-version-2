from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.db.models import Count
from django.contrib import messages
from .decorators import unauthenticated_user

# Create your views here.


@unauthenticated_user
def adminLogin(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
            
        admin = authenticate(request, username = username, password = password )

        if not admin:
            messages.add_message(request, messages.ERROR, 'Invalid username or password !')
            return render(request, "admin_login.html")

        login(request, admin)

        return redirect(reverse('resident_list'))

    return render(request, "admin_login.html")
# def adminLogin(request):
    
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         admin = auth.authenticate(username = username, password = password )

#         if admin is not None:
#             auth.login(request , admin)
#             request.session['adminLogin']=True
#             return redirect('resident_list')    
#         else:
#             messages.success(request, 'Invalid username or password')
#             return redirect("adminLogin")
#     else:
    
#         return render(request, "admin_login.html")

# def adminLogin(request):
#     msg = ''
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         admin = models.adminAccount.objects.filter(username=username, password=password).count()

#         if admin > 0:
#             request.session['adminLogin']=True
#             return redirect('resident_list')  
#         else:
#             msg = 'Invalid username or password !'
#     form = forms.adminLogin  
#     return render(request, "admin_login.html",{'form': form, 'msg': msg})
