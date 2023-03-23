from django.db import models

# Create your models here.
class User(models.Model):
    # required
    email = models.EmailField()
    password = models.CharField() # TODO: min length 8, 1 upper, 1 lower
    fullName = models.CharField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField()

    # not required
    address = models.TextField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()


class Category(models.Model):
    name=models.CharField()


class Content(models.Model):
    # required
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    pdf = models.FileField()
    
    # not required
    categories = models.ManyToManyField(Category)



