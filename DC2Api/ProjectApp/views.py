from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Project, Device, TestModel
from ProfileApp.models import Profile


from django.views.decorators.csrf import csrf_exempt

from .forms import  TestForm


def get_active_project(request, user_name):  # Получение значения активного проекта у пользователя
    if request.method == 'GET':
        try:
            user = Profile.objects.get(user__username=user_name)
            active_project = user.active_project
            project_device = active_project.device
            active_order = user.active_order
            user = str(user.user.username)
            active_project = str(active_project)
            project_device = str(project_device)
            active_order = str(active_order)
        except Exception:
            user = 'Name'
            active_project = 'active_project'
            project_device = 'project_device'
            active_order = 'active_order'
        data = {
            'user':             user,
            'active_project':   active_project,
            'project_device':   project_device,
            'active_order': active_order,
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
                    data["answer"] = project.device.title
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
                    data["answer"] = new_project.title
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


def device_for_project(request, project_name):
    data = {}
    if request.method == 'GET':
        try:
            projects = Project.objects.all()
            for project in projects:
                if project.title == project_name:
                    data["answer"] = project.title
        except Exception:
            data["answer"] = "Проект найден"
    else:
        data["answer"] = "ERROR"
    return JsonResponse(data)


@csrf_exempt
def test_file_upload(request, name):
    data = {}
    if request.method == 'PUT':
        file = request.FILES.get('file')
        print(name)
        print(file)
        data['answer'] = name
    return JsonResponse(data)


from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .serializers import FileSerializer


class FileUploadView(APIView):
    parser_classes = [FileUploadParser, JSONParser, FormParser, MultiPartParser]

    renderer_classes = [JSONRenderer]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        print(request.META.get('HTTP_TITLE'))
        #print(file_obj)
        #print(filename)
        file = TestModel(file=file_obj, title=filename)
        #print('after file')
        file.save()

        return Response(status=204)
