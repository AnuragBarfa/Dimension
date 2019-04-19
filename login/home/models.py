from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    username = models.CharField(max_length=30, blank=True, default='')
    image = models.ImageField(upload_to='image')#, default="img/profile.png"
    def __str__(self):
        return self.username

