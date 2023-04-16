from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
from django.db import models
from django.db import models

class CreditUnion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = CloudinaryField('image', default='placeholder')
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class TopicCategory(models.Model):
    name=models.CharField(max_length=200)

class Topic(models.Model):
    category=models.ForeignKey(TopicCategory,on_delete=models.CASCADE)
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,unique=True)
    summary=models.TextField(max_length=500,blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    models.SlugField(max_length=250,unique=True)
    likes = models.ManyToManyField(User, related_name='topic_like', blank=True)
    topic_trending=models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()