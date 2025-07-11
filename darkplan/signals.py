# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserTheme

@receiver(post_save, sender=User)
def create_user_theme(sender, instance, created, **kwargs):
    if created:
        UserTheme.objects.create(user=instance)
