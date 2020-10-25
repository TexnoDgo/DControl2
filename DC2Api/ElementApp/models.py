from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Assembly(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)
    draw_pdf = models.FileField(upload_to='ASSEMBLY_DRAW_PDF', default=None)
    draw_pnf = models.ImageField(upload_to='ASSEMBLY_DRAW_PNG', default=None)

    def __str__(self):
        return self.title


class Detail(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)
    draw_pdf = models.FileField(upload_to='DETAIL_DRAW_PDF', default=None)
    draw_pnf = models.ImageField(upload_to='DETAIL_DRAW_PNG', default=None)
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE, default=None)
    dxf = models.FileField(upload_to='DETAIL_DXF', default=None)
    part = models.FileField(upload_to='DETAIL_PART', default=None)

    def __str__(self):
        return self.title
