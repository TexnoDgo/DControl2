import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import Project, Profile


def get_active_project(request, url):

    if request.method == 'GET':
        try:
            user = Profile.objects.get(user__username=url)
            active_project = user.active_project
            project_device = active_project.device
        except EOFError:
            user = None
            active_project = None
            project_device = None

        data = {
            'user':             user,
            'active_project':   active_project,
            'project_device':   project_device
        }

        tmpJson = serializers.serialize("json", data)
        tmpObj = json.loads(tmpJson)

        return JsonResponse(json.dumps(tmpObj))




