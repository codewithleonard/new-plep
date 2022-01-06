from django.urls import path
from . import views
from .apps import ApiConfig

app_name = ApiConfig.name

urlpatterns = [
    path('<str:pk>/', views.getClient, name="getClient"),
]
