from django.db.models.signall import post_save
from django.contrib.auth import get_user_model
from django.dispatch import reciever 
from .models import Profile


@reciever(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.object.create(user=instance)


@reciever(post_save, sender=get_user_model())
def save_profile(sender, instance, created, **kwargs):
    instance.Profile.save()
