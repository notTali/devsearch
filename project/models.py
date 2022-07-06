from email.policy import default
from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, null=False, blank=False, primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=200)
    description = models.TextField(null=True, blank=True)
    #owner
    featured_image = models.ImageField(null=True, blank=True, default='Design.JPG', upload_to='static/images/')
    demo_link = models.CharField(null=True, blank=True, max_length=200)
    source_code = models.CharField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    #vote_ratio
    #vote_count

    def __str__(self):
        return self.title

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name