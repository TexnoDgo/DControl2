from django.urls import path
from .views import get_active_project, get_projects_list, get_devices_lsit, change_active_device, create_project

urlpatterns = [
    path(r'get_active_project/<url>', get_active_project, name='get_active_project'),
    path(r'get_projects_list', get_projects_list, name='get_projects_list'),
    path(r'get_devices_lsit', get_devices_lsit, name='get_devices_lsit'),
    path(r'change_active_device/<user_name>/<project_name>', change_active_device, name='change_active_device'),
    path(r'create_project/<project_name>/<device_name>/<user_name>/<choose>', create_project, name='create_project'),

]
