"""
URL configuration for demopro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodmorning',views.GoodMorning.as_view(),name='goodmorning'),
    path('goodevening',views.GoodMorning.as_view(),name='goodevening'),
    path('helloworld',views.HelloWorld.as_view(),name='helloworld'),
    path('userdetails',views.UserDetails.as_view(),name='userdetails'),
    path('studentdetails',views.StudentDetails.as_view(),name='studentdetails'),
    path('studentcreate',views.StudentCreate.as_view(),name='studentcreate'),
    path('studentdetail/<int:i>',views.StudentDetail.as_view(),name='studentdetail'),
    path('studentdelete/<int:i>',views.StudentDelete.as_view(),name='studentdelete'),
    path('studentfullupdate/<int:i>',views.StudentFullUpdate.as_view(),name='studentfullupdate'),
    path('studentpartialupdate/<int:i>',views.StudentPartialUpdate.as_view(),name='studentpartialupdate'),
]
