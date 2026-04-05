from django.shortcuts import render, redirect
from profileapp.models import Profile
from django.contrib.auth.models import User


# Create your views here.
def _get_profile_by_email(email):
    try:
        return Profile.objects.get(email=email)
    except Profile.DoesNotExist:
        return None

def profileView(request):

    user = request.user

    try:
        profile = Profile.objects.get(email=user.email)
    except Profile.DoesNotExist:
        profile = None

    return render(request,'profile.html',{
        'profile':profile
    })

def edit_profileview(request):

    user = request.user

    try:
        profile = Profile.objects.get(email=user.email)
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":

        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        if profile:
            profile.fullname = fullname
            profile.contact = contact
            profile.gender = gender
            if image:
                profile.image = image
            profile.save()
        else:
            Profile.objects.create(
                fullname=fullname,
                email=user.email,
                contact=contact,
                gender=gender,
                image=image
            )

        return redirect('profile')

    return render(request,'editprofile.html',{
        'profile':profile
    })