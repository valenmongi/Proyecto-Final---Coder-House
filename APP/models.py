from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    project_manager = models.CharField(max_length=100)
    user_in_charge = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='project_images', null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return {self.title}, {self.project_manager}


class Users(models.Model):
    user_name = models.EmailField()
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)

class Purchases(models.Model):
    user_name = models.EmailField()
    date_purchase = models.DateField(max_length=10)
    purchase = models.CharField(max_length=50)
    price_purchase = models.IntegerField()

class Publications(models.Model):
    user_name = models.EmailField()
    date_publication = models.DateField(max_length=10)
    publication = models.CharField(max_length=50)
    price_publication = models.IntegerField()
    publication_sell = models.BooleanField()
