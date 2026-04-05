from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courseapp.models import Course, CourseRating
from checkout.models import Checkout
from django.contrib import messages


@login_required
def specificCourseDetail(request, id):

    course = get_object_or_404(Course, id=id)

    is_enrolled = Checkout.objects.filter(
        user=request.user,
        course=course,
        payment_status=True
    ).exists()


    user_rating = None


    if request.user.is_authenticated:

        rating_obj = CourseRating.objects.filter(
            user=request.user,
            course=course
        ).first()

        if rating_obj:
            user_rating = rating_obj.rating


    if request.method == "POST":

        rating_value = request.POST.get("rating")

        if rating_value:

            CourseRating.objects.update_or_create(
                user=request.user,
                course=course,
                defaults={"rating": rating_value}
            )

            user_rating = int(rating_value)
            messages.success(request, " Your rating has been submitted successfully!")


    return render(request, "coursedetail.html", {

        "course": course,
        "is_enrolled": is_enrolled,
        "user_rating": user_rating

    })