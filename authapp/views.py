from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courseapp.models import Course
from checkout.models import Checkout




# Create your views here.
def home(req):

    courses = Course.objects.all()
    enrolled_ids = []

    if req.user.is_authenticated:
        enrolled_ids = Checkout.objects.filter(
            user=req.user,
            payment_status=True
        ).values_list('course_id', flat=True)

    return render(req, 'index.html', {
        'courses': courses,
        'enrolled_ids': enrolled_ids
    })
def aboutView(req):
    return render(req, 'about.html')

def contactView(req):
    if req.method == "POST":
        messages.success(req, "Thank you! Your message has been sent. We'll get back to you shortly.")
        return redirect('/contact')
    return render(req, 'contact.html')

def loginView(req):
    if req.method=="POST":
        data=req.POST
        username=data.get("username")
        password=data.get("password")

        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(req,user)
            messages.success(req, 'Login Successfully!!')
            return redirect("/")
        else:
            messages.error(req, 'Invalid Credentials')
            return redirect("/login")

    return render(req,'login.html')


def registerView(req):
    if req.method=="POST":
        data=req.POST
        username=data.get("username")
        email=data.get("email")
        password=data.get("password")
        User.objects.create_user(username=username,email=email,password=password)
        messages.success(req,'register successfully!!')
        return redirect('/login')
    
    return render(req,'register.html')

def logoutView(req):
    logout(req)
    messages.success(req, "Logout Successfull.")
    return redirect("/login")

@login_required(login_url="/login")
def programView(req):
    courses = Course.objects.all()
    
    # Get list of course IDs the user has already enrolled in
    enrolled_ids = Checkout.objects.filter(
        user=req.user,
        payment_status=True
    ).values_list('course_id', flat=True)

    return render(req, 'course.html', context={
        "courses": courses,
        "enrolled_ids": enrolled_ids
    })