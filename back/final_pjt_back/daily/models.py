from django.db import models

# Create your models here.
class Youtube(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_url = models.TextField()
    video_id = models.TextField()