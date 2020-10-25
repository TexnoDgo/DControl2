from django.urls import path
from .views import create_order, get_order_list_for_project, change_active_order

urlpatterns = [
    path(r'create_order/<order_name>/<project_name>/<user_name>/<choose>', create_order, name='create_order'),
    path(r'get_order_list_for_project/<project_name>', get_order_list_for_project, name='get_order_list_for_project'),
    path(r'change_active_order/<user_name>/<order_name>', change_active_order, name='change_active_order'),
]
