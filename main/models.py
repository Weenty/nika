from django.db import models
from django.contrib.auth.models import AbstractUser

class users(AbstractUser):
    phone_number = models.CharField(max_length=45)

    def __str__(self):
        return self.username

class section(models.Model):
    name = models.CharField(max_length=45)

class caterogy(models.Model):
    name = models.CharField(max_length=45)
    section = models.ManyToManyField(section)
    def __str__(self):
        return self.name

class catalogy(models.Model):
    name = models.CharField(max_length=45)
    discription = models.TextField(default='')
    cost = models.DecimalField(max_digits=7, decimal_places=0)
    discount = models.IntegerField(default=0)
    img = models.ImageField(upload_to=f'uploads/{name}/')
    quantity = models.IntegerField(default=0)
    purpose = models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=45, default='')
    procer = models.CharField(max_length=45, default='')
    best_before_date = models.DateField(default='')
    composition = models.CharField(max_length=255, default='')
    # package = здесь как-то нужно выбдвинуть разновидности упаковок     
    rating = models.FloatField(default=0)
    number_of_views = models.IntegerField(default=0)
    category = models.ManyToManyField(caterogy)
    def __str__(self):
        return self.name

