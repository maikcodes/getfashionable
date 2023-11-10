from django.db import models
from django.contrib.auth.models import User

import uuid

from .Collection import Collection


class Design(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='designs', null=False)
    image_width = models.IntegerField(default=200)
    image_height = models.IntegerField(default=200)
    
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Methods to store designs in specific routes

def user_upload_to(instance, filename):
    return f'user_images/{instance.user.id}/{uuid.uuid4()}/{filename}'


def design_upload_to(instance, filename):
    return f'designs/{uuid.uuid4()}/{filename}'


def collection_upload_to(instance, filename):
    return f'collections/{instance.collection.id}/{uuid.uuid4()}/{filename}'
