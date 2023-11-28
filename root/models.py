from django.db import models
from accounts.models import CustomeUser
# Create your models here.

class Services (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    

class NewsLetter (models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name
    



class Team(models.Model):
    firstname = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    job = models.ManyToManyField()
    description = models.TextField()
    image = models.ImageField(upload_to='trainer', default='teacher.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
   
   



    


class Price(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    properties = models.CharField(max_length = 80)
    def __str__(self):
        return self.title
