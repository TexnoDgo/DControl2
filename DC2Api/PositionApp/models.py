from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from OrderApp.models import Order
from ElementApp.models import Detail, Assembly


class Position(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, default=None)
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField()
    code = models.CharField(max_length=13)
    qr_code = models.ImageField(upload_to='POSITION_QR_CODE', default=None)
    sticker = models.FileField(upload_to='POSITION_STICKER', default=None)
    draw_pdf = models.FileField(upload_to='POSITION_DRAW_PDF', default=None)

    def __str__(self):
        return self.order.title

