from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# create your views here.

def home(request):
    return render(request, "authentication/home.html")

def signup(request):

    if request.method == "POST":
        Username = request.POST.get('Username')
        Fname = request.POST.get('First Name')
        Lname = request.POST.get('Last name')
        Email = request.POST.get('email')
        Pass1 = request.POST.get('Pass1')
        Pass2 = request.POST.get('Pass2')

        myuser = User.objects.create(Username, Email, Pass1)
        myuser.First_name = Fname
        myuser.Last_name = Lname
       
        myuser.save()

        messages.success(request, "Your Account Has Been Succeefuly created")

        return redirect(signin)

    return render(request,"authenticatin/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass     