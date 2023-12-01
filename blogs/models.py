
from django.db import models
from accounts.models import CustomeUser



class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name   
    

 






class Post(models.Model):
    image =models.ImageField(upload_to='blog', default='default.jpg')
    author = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    #comments
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    counted_comments = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-created_date',)


    def __str__(self):
        return self.title
    

    def snipest(self):
        return " ".join(self.content.split()[:3])


class Comments(models.Model):
    which_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return self.name
    

class Replay(models.Model):
    which_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return str(self.which_comment)