from django.contrib.auth import authenticate, login as auth_login
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User



# Create your views here.


def register(request):
    context = {}
    if request.method == "GET":
        return render(request, 'registerpage.html')
    else:
        usrname = request.POST['uname']
        password = request.POST['upasswd']
        firstname= request.POST['ufname']
        lastname= request.POST['ulname']
        email = request.POST['uemail']
        if usrname == '' or password == '' or email == '' or firstname=='' or lastname=='':
            context['errmsg'] = "Fields cannot be empty"
            return render(request, "registerpage.html", context)
        else:
            try:
                u = User.objects.create(username=usrname,first_name=firstname,last_name=lastname,email=email)
                u.set_password(password)
                u.save()
                context['success']="User created successfully"
                return redirect('')
            except Exception:
                context['Errmsg']="User already Exists"
                return render(request,'registerpage.html',context)  

def login(request):
    context = {}
    if request.method == "GET":
        return render(request, 'loginpage.html')
    else:
        uname = request.POST['uname']
        passwd = request.POST['upasswd']
        user = authenticate(request, username=uname, password=passwd)
        if user is not None:
            auth_login(request, user)
            return redirect('/index')
        else:
            context['auth_failed'] = True
            context['errmsg'] = "Invalid Username and Password!!!"
            return render(request, 'loginpage.html', context)


def Index(request):
    return render(request,'index.html')

def phones(request):
    return render(request,'phones.html')




