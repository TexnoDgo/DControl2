from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ProjectApp.models import Project


class Order(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    readiness = models.DateField(null=True)
    table = models.FileField(upload_to="ORDERS_TABLE", default=None)
    qr_code_list = models.FileField(upload_to='ORDERS_QR_CODE_LIST', default=None)
    pdf_specification = models.FileField(upload_to='ORDER_PDF_SPECIFICATION', default=None)
    draw_archive = models.FileField(upload_to='ORDERS_DRAW_ARCHIVE', default=None)
    dxf_archive = models.FileField(upload_to='ORDERS_DXF_ARCHIVE', default=None)
    part_archive = models.FileField(upload_to='ORDERS_PART_ARCHIVE', default=None)

    def __str__(self):
        return self.title
