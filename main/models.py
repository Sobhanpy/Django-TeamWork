from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomeUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length= 255) 
    client_url = models.CharField(max_length=255, default='#') 
    client = models.ForeignKey(CustomeUser, on_delete= models.CASCADE)
    content = models.TextField()
    image1 = models.ImageField(upload_to= 'blog')
    image2 = models.ImageField(upload_to= 'blog')
    image3 = models.ImageField(upload_to= 'blog')
    published_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ('-created_date',)

# Create your models here.

