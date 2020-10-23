from django.shortcuts import render
from django.http import JsonResponse
from ProjectApp.models import Project, Profile, Device
from .models import Order
# Create your views here.


def create_order(request, order_name, project_name, user_name, choose):  # Создание нового заказ
    print('create')
    # Опционально изминение активного заказ
    data = {}
    if request.method == 'GET':
        print('GET')
        try:
            projects = Project.objects.all()
            user = Profile.objects.get(user__username=user_name)
            print('Ok1')
            for project in projects:
                if project.title == project_name:
                    new_order = Order(title=order_name, author=user.user, project=project)
                    new_order.save()
                    data["answer"] = new_order
                    print('Ok2')
            if choose == 'choose':
                user.active_order = new_order
                user.save()
        except Exception:
            data["answer"] = "Пользователь не найден"
    else:
        data["answer"] = "ERROR"
        print('NoPOST')
    return JsonResponse(data)
