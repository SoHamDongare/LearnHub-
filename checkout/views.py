
from django.shortcuts import render,redirect
from courseapp.models import Course
from checkout.models import Checkout


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from courseapp.models import Course
from checkout.models import Checkout


def checkout(req):
    cart = req.session.get('cart', {})
    items = []
    grand_total = 0
    invalid_ids = []

    for course_id, quantity in cart.items():
        try:
            course = Course.objects.get(id=course_id)
            subtotal = course.price * quantity
            grand_total += subtotal
            items.append({
                'course': course,
                'quantity': quantity,
                'subtotal': subtotal
            })
        except Course.DoesNotExist:
            invalid_ids.append(course_id)

    for bad_id in invalid_ids:
        del cart[bad_id]
    if invalid_ids:
        req.session['cart'] = cart
        req.session.modified = True

    grand_total_discount = grand_total - grand_total * 0.15

    return render(req, 'checkout.html', {
        'items': items,
        'grand_total': grand_total,
        'grand_total_discount': grand_total_discount
    })


def payment(req):
    return render(req, 'payment.html')


def dummyPayment(req):
    if req.method == "POST":
        return render(req, 'dummypayment.html')
    return redirect('/payment')


@login_required(login_url="/login")
def success(req):
    if req.method == "POST":
        cart = req.session.get('cart', {})

        for course_id, quantity in cart.items():
            try:
                course = Course.objects.get(id=course_id)
                already_exists = Checkout.objects.filter(
                    user=req.user,
                    course=course
                ).exists()
                if not already_exists:
                    Checkout.objects.create(
                        user=req.user,
                        course=course,
                        amount=course.price,
                        payment_status=True
                    )
            except Course.DoesNotExist:
                pass

        req.session['cart'] = {}
        req.session.modified = True
        return render(req, 'success.html')

    return redirect('/payment')