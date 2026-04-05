from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Checkout

# Create your views here.


@login_required(login_url="/login")
def my_courses(request):
    enrollments = Checkout.objects.filter(user=request.user, payment_status=True)
    return render(request, 'mycourses.html', {'enrollments': enrollments})


@login_required(login_url="/login")
def enroll_course(request, id):
    from courseapp.models import Course
    course = Course.objects.get(id=id)

    # Check if already enrolled
    already_enrolled = Checkout.objects.filter(
        user=request.user,
        course=course,
        payment_status=True
    ).exists()

    if already_enrolled:
        messages.warning(request, f'You are already enrolled in "{course.name}"!')
        return redirect('/course')
    else:
        # Add to cart and redirect to checkout
        request.session.setdefault('cart', {})
        request.session['cart'][str(id)] = 1
        request.session.modified = True
        return redirect('/checkout')

@login_required(login_url="/login")
def unenroll_course(request, id):
    from courseapp.models import Course
    from checkout.models import Checkout
    course = Course.objects.get(id=id)

    enrollment = Checkout.objects.filter(
        user=request.user,
        course=course,
        payment_status=True
    ).first()

    if enrollment:
        enrollment.delete()
        messages.success(request, f'You have successfully unenrolled from "{course.name}".')
    else:
        messages.error(request, 'No enrollment found.')

    return redirect('/mycourses/')