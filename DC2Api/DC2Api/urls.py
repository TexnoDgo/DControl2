from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('ProjectApp.urls')),
    path('order/', include('OrderApp.urls')),
]
