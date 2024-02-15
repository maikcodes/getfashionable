from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

from .Collection import Collection
import uuid


def image_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{extension}"
    
    if instance.collection:
        collection_id = instance.collection.id
        return  f"images/collection/{collection_id}/{filename}"
    else: 
        user_id = instance.user.id
        return f"images/designs/{user_id}/{filename}"


class Design(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to=image_path, null=False)
    image_width = models.PositiveIntegerField(default=200)
    image_height = models.PositiveIntegerField(default=200)
    description = models.TextField(blank=True)
    
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
