from pyexpat import model
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class section_and_caterogy(MPTTModel):
    name = models.CharField(max_length=20)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name']
    
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

class rating(models.Model):
    rating = models.FloatField(default=0)

class products(models.Model):
    name = models.CharField(max_length=45)
    discription = models.TextField(default='')
    discount = models.IntegerField(default=0)
    purpose = models.CharField(max_length=255, default='')
    brand = models.CharField(max_length=45, default='')
    manufacturer = models.CharField(max_length=45, default='')
    best_before_date = models.DateField(default='')
    composition = models.CharField(max_length=255, default='')
    rating = models.OneToOneField(rating, on_delete=models.PROTECT)
    number_of_views = models.IntegerField(default=0)
    category = models.ManyToManyField('section_and_caterogy', through='product_has_section_and_category')
    package = models.ManyToManyField('package', through='product_has_packages')
    def __str__(self):
        return self.name

class product_has_packages(models.Model):
    product = models.ForeignKey(products, on_delete=models.PROTECT)
    package = models.ForeignKey(package, on_delete=models.PROTECT)

class product_has_section_and_category(models.Model):
    product = models.ForeignKey(products, on_delete=models.PROTECT)
    section_and_caterogy = models.ForeignKey(section_and_caterogy, on_delete=models.PROTECT)
    
