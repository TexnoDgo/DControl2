from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ProjectApp.models import Project
from OrderApp.models import Order


class Profile(models.Model):
    ROOT_STATUS_LIST = (
        ('DESIGNER', 'DESIGNER'),
        ('PRODUCTION', 'PRODUCTION'),
        ('GUEST', 'GUEST')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    root_status = models.CharField(max_length=100, choices=ROOT_STATUS_LIST, default='GUEST')
    active_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    active_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Profile: " + self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
