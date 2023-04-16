from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class CreditUnion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = CloudinaryField('image', default='placeholder')
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name