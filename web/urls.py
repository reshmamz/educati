"""PROJECT1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.conf.urls import url
urlpatterns = [
    path('',views.dashboard),
    path('login/', views.login_view),
    path('resetpassword/',views.forgot),
    path('about/',views.about),
    path('notification/',views.emailnoti),
    path('career/',views.career),
    path('contact/',views.contact),
    path('events/',views.events),
    path('courses/',views.courses),
    url(r'^faculty/(?P<id>\d+)/$',views.faculy),
    path('gallery/',views.gallery),
    url(r'^pass/(?P<uid>\d+)/(?P<id>\d+)/$',views.passwrd),
    url(r'^coursedetails/(?P<id>\d+)/$',views.coursedetails),
    url(r'^eventdetails/(?P<id>\d+)/$',views.eventdetails),
    url(r'^careerapply/(?P<id>\d+)/$',views.careerapply),
]
