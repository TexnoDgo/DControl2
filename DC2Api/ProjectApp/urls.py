from django.urls import path
from .views import get_active_project

urlpatterns = [
    path(r'get_active_project/<url>', get_active_project, name='get_active_project'),
]
