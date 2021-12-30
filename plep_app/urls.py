from django.urls import path
from . import views
from .apps import PlepAppConfig

app_name = PlepAppConfig.name

urlpatterns = [
     path('', views.index, name="home"),
     path('csc320/', views.csc320, name="csc320"),
     path('register/', views.register, name="register"),
     path('uid_verification/', views.uid_verification, name="uid_verification")
]
