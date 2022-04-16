from django.db import models


class section(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class caterogy(models.Model):
    name = models.CharField(max_length=45)
    section = models.ManyToManyField(section)
    def __str__(self):
        return self.name


class image(models.Model):
    image = models.ImageField(upload_to='uploads/')


class package(models.Model):
    name = models.CharField(max_length=45)
    cost = models.DecimalField(max_digits=7, decimal_places=0)
    quantity = models.IntegerField(default=0)
    image = models.OneToOneField(image, on_delete=models.PROTECT, default='')
    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length=45)
    discription = models.TextField(default='')
    discount = models.IntegerField(default=0)
    purpose = models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=45, default='')
    manufacturer = models.CharField(max_length=45, default='')
    best_before_date = models.DateField(default='')
    composition = models.CharField(max_length=255, default='')
    rating = models.FloatField(default=0)
    number_of_views = models.IntegerField(default=0)
    category = models.ManyToManyField(caterogy)
    package = models.ForeignKey(package, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

