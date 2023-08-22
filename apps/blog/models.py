from django.db import models
from application.custom_models import DateTimeModel
# Create your models here.

class Blog(DateTimeModel):

    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title
