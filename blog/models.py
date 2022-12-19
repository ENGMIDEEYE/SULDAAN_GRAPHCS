from django.db import models

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to = 'static/images')
    Desc = models.TextField()
    Publish = models.BooleanField(default=True)
    Tags = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

class Visitors(models.Model):
    Name = models.CharField(max_length=50)
    Desc = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'Visitors'

class Management(models.Model):
    Name = models.CharField(max_length=50)
    Desc = models.TextField()
    Image = models.ImageField(upload_to = 'static\Management_photos')
    Email = models.EmailField()
    Facebook = models.CharField(max_length=100,unique=True)
    Twitter = models.CharField(max_length=100,unique=True)
    Whatsapp = models.CharField(max_length=100,unique=True)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name_plural = 'Management'

    
