from django.db import models
class  Client(models.Model):
    rasm = models.ImageField(upload_to='rasm/images')
    nomi = models.CharField(max_length=200)
    hotelnomi = models.CharField(max_length=200)
    narxi = models.CharField(max_length=222)
    text = models.TextField()
    rating = models.CharField(max_length=200)

# Create your models here.
class Email(models.Model):
    email = models.CharField(max_length=222)
