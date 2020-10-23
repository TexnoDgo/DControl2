from django.urls import path
from .views import create_order

urlpatterns = [
    path(r'create_order/<order_name>/<project_name>/<user_name>/<choose>', create_order, name='create_order'),
]
