from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Project, Profile, Device


def get_active_project(request, url):  # Получение значения активного проекта у пользователя
    if request.method == 'GET':
        try:
            user = Profile.objects.get(user__username=url)
            active_project = user.active_project
            project_device = active_project.device
            active_order = user.active_order
            user = str(user.user.username)
            active_project = str(active_project)
            project_device = str(project_device)
        except Exception:
            user = 'Name'
            active_project = 'active_project'
            project_device = 'project_device'
        data = {
            'user':             user,
            'active_project':   active_project,
            'project_device':   project_device
        }
        return JsonResponse(data)


def get_projects_list(request):  # Поучение списка всех проектов
    if request.method == 'GET':
        data = {}
        try:
            all_projects = Project.objects.all()
            i = 1
            for project in all_projects:
                data[i] = project.title
                i += 1
        except Exception:
            data[1] = "Список проектов пуст"
        return JsonResponse(data)


def get_devices_lsit(request):  # Получение списка девайсов
    if request.method == 'GET':
        data = {}
        try:
            all_devices = Device.objects.all()
            i = 1
            for device in all_devices:
                data[i] = device.title
                i += 1
        except Exception:
            data[1] = "Список девайсов пуст"
        return JsonResponse(data)


def change_active_device(request, user_name, project_name):  # Изминеине активного проекта для пользователя
    data = {}
    if request.method == 'GET':
        try:
            user = Profile.objects.get(user__username=user_name)
            all_projects = Project.objects.all()
            for project in all_projects:
                if project.title == project_name:
                    user.active_project = project
                    user.save()
                    data["answer"] = project_name
        except Exception:
            data["answer"] = "Пользователь не найден"
    else:
        data["answer"] = "ERROR"
    return JsonResponse(data)


def create_project(request, project_name, device_name, user_name, choose):  # Создание нового проекта.
    print('create')
    # Опционально изминение активного проекта
    data = {}
    if request.method == 'GET':
        print('GET')
        try:
            devices = Device.objects.all()
            user = Profile.objects.get(user__username=user_name)
            print('Ok1')
            for device in devices:
                if device.title == device_name:
                    new_project = Project(title=project_name, author=user.user, device=device)
                    new_project.save()
                    data["answer"] = new_project
                    print('Ok2')
            if choose == 'choose':
                user.active_project = new_project
                user.save()
        except Exception:
            data["answer"] = "Пользователь не найден"
    else:
        data["answer"] = "ERROR"
        print('NoPOST')
    return JsonResponse(data)
