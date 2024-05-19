"""
URL configuration for evenmanageproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from evenapp import views
from evenmanageproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('services',views.service,name='services'),
    path('booking',views.booking,name='booking'),
    path('suggestions',views.review_page,name='suggestions'),
    path('contact',views.contact_page,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout/', views.logout, name='logout')
]


if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)