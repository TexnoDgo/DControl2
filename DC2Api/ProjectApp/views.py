from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Project, Profile


def get_active_project(request, url):

    if request.method == 'GET':
        try:
            user = Profile.objects.get(user__username=url)
            active_project = user.active_project
            project_device = active_project.device
            print('try')
            user = str(user.user.username)
            active_project = str(active_project)
            project_device = str(project_device)
            print(user)
            print(active_project)
            print(project_device)
        except Exception:
            user = 'Name'
            active_project = 'active_project'
            project_device = 'project_device'
            print('except')

        #user = 'Name'
        #active_project = 'active_project'
        #project_device = 'project_device'

        data = {
            'user':             user,
            'active_project':   active_project,
            'project_device':   project_device
        }

        return JsonResponse(data)
    #return redirect(request.META['HTTP_REFERER'])




