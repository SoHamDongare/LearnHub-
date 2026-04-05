from django.shortcuts import render, redirect
from courseapp.models import Course


def view_cart(request):
    cart = request.session.get('cart', {})
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
        request.session['cart'] = cart
        request.session.modified = True

    return render(request, 'course_cart.html', {
        'items': items,
        'grand_total': grand_total
    })


def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1
    request.session['cart'] = cart
    return redirect('/cart/')


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    return redirect('/cart/')