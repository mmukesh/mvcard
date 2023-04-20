from django.db import models
import PIL.Image as Image

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null= True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='media')
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    phone =models.CharField(max_length=15,null=True,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='media',null=True,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    phone =models.CharField(max_length=15,null=True,blank=True)
    product = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='media')
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
