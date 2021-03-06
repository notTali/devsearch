import email
from django.db import models
from django.contrib.auth.models import User 
import uuid

from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, null=False, blank=False, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='static/images/profiles/')

    def __str__(self):
        return str(self.name)

def profileUpdated(sender, instance, created, **kwargs):
    print('profile saved!')
    print('instance: ', instance)
    print('sender: ', sender)
    print('created: ', created)

post_save.connect(profileUpdated, sender=Profile)