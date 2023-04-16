from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    First_name = models.CharField(max_length=200, null=True)
    Second_name = models.CharField(max_length=200, null=True)
    credit_union = models.ForeignKey(CreditUnion, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True, null=True)
    profile_pic = models.ImageField(null=True, default="placeholder")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class CreditUnion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = CloudinaryField('image', default='placeholder')
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name