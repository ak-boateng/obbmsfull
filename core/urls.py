from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('donor', views.donor, name='donor'),
    path('administrator', views.administrator, name='administrator'),
    path('adminsignup', views.adminsignup, name='adminsignup'),
    path('login', views.adminlogin, name='login'),
    path('donorlogin', views.donorlogin, name='donorlogin'),
    path('donorsignup', views.donorsignup, name='donorsignup'),
    path('requestblood', views.requestblood, name='requestblood'),
    path('done', views.done, name='done'),
    path('logout', views.logoutView, name='logout'),
    path('admins', views.admins, name='admins'),
    path('details/<str:dn>', views.details, name='details'),
]
