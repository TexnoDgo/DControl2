from django.contrib import admin
from .models import Device, Project, TestModel
from ProfileApp.models import Profile


admin.site.register(Profile)
admin.site.register(Device)
admin.site.register(Project)
admin.site.register(TestModel)

