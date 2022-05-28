from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100 ,null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100 ,null=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True ,blank=True)
    image = models.ImageField(upload_to='images')
    # video = models.FileField(null=False, blank=False)

    description = models.TextField(blank=True)


    def __str__(self):
        return self.title
