
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plep_app.urls', namespace="plep_app")),
    path('api/', include('api.urls', namespace="api"))
]
