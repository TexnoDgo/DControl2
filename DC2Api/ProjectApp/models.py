from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver


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

    def __str__(self):
        return self.title


class Profile(models.Model):
    ROOT_STATUS_LIST = (
        ('DESIGNER', 'DESIGNER'),
        ('PRODUCTION', 'PRODUCTION'),
        ('GUEST', 'GUEST')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    root_status = models.CharField(max_length=100, choices=ROOT_STATUS_LIST, default='GUEST')
    active_project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Profile: " + self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
