"""
URL configuration for AuthProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authapp import views
from django.conf.urls.static import static
from django.conf import settings
from courseapp.views import specificCourseDetail
from profileapp.views import  edit_profileview, profileView
from cartapp import views as cart_views
from checkout.views import checkout,payment,dummyPayment,success
from mycourseapp.views import my_courses, enroll_course,unenroll_course
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about', views.aboutView, name='about'),
    path('contact', views.contactView, name='contact'),
    path('login',views.loginView),
    path('register',views.registerView),
    path('logout',views.logoutView),
    path('course',views.programView),
    path('detail/<int:id>', specificCourseDetail),
    path('profile/',profileView, name='profile'),
    path('edit/', edit_profileview, name='profile_edit'),
    path('cart/', cart_views.view_cart, name='view_cart'),
    path('cart/add/<int:id>/', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('checkout',checkout),
    path('payment',payment),
    path('dummypayment',dummyPayment),
    path('success',success),
    path('mycourses/', my_courses, name='my_courses'),
    path('enroll/<int:id>/',enroll_course,name='enroll_course'),
    path('unenroll/<int:id>/', unenroll_course, name='unenroll'),
]
    
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
