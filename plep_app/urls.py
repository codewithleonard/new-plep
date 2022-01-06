from django.urls import path
from . import views

app_name = "plep_app"

urlpatterns = [
     path('', views.index, name="home"),
     path('csc320/', views.csc320, name="csc320"),
     path('register/', views.register, name="register"),
     path('reg_success/', views.reg_success, name="reg_success"),
     path('uid_verification/', views.uid_verification, name="uid_verification"),
     path('uid_verification/dashboard/<str:pk>/', views.dashboard, name="dashboard"),
]
