from turtle import title
from uuid import uuid4
from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, null=False, blank=False, primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=200)
    description = models.TextField(null=True, blank=True)
    #owner
    # featured_image = models.ImageField(null=True, blank=True)
    demo_link = models.CharField(null=True, blank=True, max_length=200)
    source_code = models.CharField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    #tags
    #vote_ratio
    #vote_count
