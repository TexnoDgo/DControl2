from django.contrib import admin
from .models import Device, Project, Profile


admin.site.register(Profile)
admin.site.register(Device)
admin.site.register(Project)
