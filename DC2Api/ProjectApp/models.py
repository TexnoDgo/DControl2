from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Device(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    pdf_specification = models.FileField(upload_to='PROJECT_PDF_SPECIFICATION', default=None)

    def __str__(self):
        return self.title


class TestModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='TEST_FILE')

    def __str__(self):
        return self.title