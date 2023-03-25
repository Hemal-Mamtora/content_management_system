from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # required
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) # TODO: min length 8, 1 upper, 1 lower
    fullName = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)

    # not required
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    USER_ROLES=(
        ('ADMIN','ADMIN'),
        ('AUTHOR','AUTHOR'),
    )
    user_type=models.CharField(choices=USER_ROLES, max_length=16, default='AUTHOR')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self) -> str:
        return self.email


class Category(models.Model):
    name=models.CharField(max_length=255)


class Content(models.Model):
    # required
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    pdf = models.FileField()
    
    # not required
    categories = models.ManyToManyField(Category)



