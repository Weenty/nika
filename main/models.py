from django.db import models
from django.contrib.auth.models import AbstractUser
from goods.models import products


class users(AbstractUser):
    phone_number = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    basket = models.ForeignKey('basket', on_delete=models.PROTECT, default='')
    orders = models.ForeignKey('orders', on_delete=models.CASCADE, default='', null=True)
    def __str__(self):
        return self.username

class basket(models.Model):
    id = models.AutoField(unique=False, primary_key=True)
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered = models.IntegerField(default=0)

class paymant_method(models.Model):
    name = models.CharField(max_length=45)

class receiving_method(models.Model):
    name = models.CharField(max_length=45) 

class point_of_issue(models.Model):
    index = models.CharField(max_length=45)
    sity = models.CharField(max_length=45)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=45)

class orders(models.Model):
    id_basket = models.ForeignKey('basket', on_delete=models.CASCADE)
    final_cost = models.DecimalField(max_digits=7, decimal_places=0)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    comment = models.TextField()
    payment_method = models.OneToOneField(paymant_method, on_delete=models.PROTECT)
    receiving_method = models.OneToOneField(receiving_method, on_delete=models.PROTECT)
    point_of_issue = models.OneToOneField(point_of_issue, on_delete=models.PROTECT)