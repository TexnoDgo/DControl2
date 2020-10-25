from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from ProjectApp.models import Project, Device
from ProfileApp.models import Profile

# Create your views here.


def create_order(request, order_name, project_name, user_name, choose):  # Создание нового заказ
    # Опционально изминение активного заказ
    data = {}
    if request.method == 'GET':
        try:
            projects = Project.objects.all()
            user = Profile.objects.get(user__username=user_name)
            for project in projects:
                if project.title == project_name:
                    new_order = Order(title=order_name, author=user.user, project=project)
                    new_order.save()
                    data["answer"] = new_order
            if choose == 'choose':
                user.active_order = new_order.title
                user.active_project = new_order.project
                user.save()
        except Exception:
            data["answer"] = "Пользователь не найден"
    else:
        data["answer"] = "ERROR"
    return JsonResponse(data)


def get_order_list_for_project(request, project_name):
    print('get_order_list_for_project')
    data = {}
    if request.method == 'GET':
        print('GET')
        try:
            print('tri')
            projects = Project.objects.all()
            for project in projects:
                if project.title == project_name:
                    project_orders = Order.objects.filter(project=project)
                    i = 1
                    for order in project_orders:
                        data[i] = order.title
                        i += 1
                        print(i)
        except Exception:
            data["answer"] = "Список заказов пуст"
    else:
        data["answer"] = "ERROR"
    return JsonResponse(data)


def change_active_order(request, user_name, order_name):
    data = {}
    if request.method == 'GET':
        try:
            orders = Order.objects.all()
            user = Profile.objects.get(user__username=user_name)
            for order in orders:
                if order.title == order_name:
                    user.active_order = order
                    user.active_project = order.project
                    user.save()
                    data["answer"] = order.title
        except Exception:
            data["answer"] = "Пользователь не найден"
    else:
        data["answer"] = "ERROR"
    return JsonResponse(data)
