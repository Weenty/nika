from django.db import models
from django.contrib.auth.models import AbstractUser
from goods.models import products, package
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from goods.models import product_has_packages

class users(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    phone_number = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

class comments(models.Model):
    user = models.ForeignKey('users', on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(default='', null=True, blank=True)
    grade = models.SmallIntegerField(
        null=False, 
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )
    def __str__(self):
        return str(self.grade)

    def calculate_rating(self):
        return self.grade, self.products

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

@receiver(post_save, sender=comments)
def Calculate_rating(sender, instance, created, *args, **kwargs):
    grade, product = instance.calculate_rating()
    result_rating = 0
    comments_list = comments.objects.filter(products=product)
    for grade in comments_list:
        result_rating += getattr(grade, 'grade')
    new_rate = getattr(product, 'rating')
    new_rate.rating = result_rating/len(comments_list)
    new_rate.save()

class basket(models.Model):
    user = models.ForeignKey('users', on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    package = models.ForeignKey(package, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.products} {self.package} user {self.user}'
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары корзины'

    def save(self, *args, **kwargs):
        packages = product_has_packages.objects.filter(product=self.products.id)
        flag = False
        for package in packages:
            if self.package == getattr(package, 'package'):
                flag = True
                break
        if flag:
            super().save(*args, **kwargs)
        else: 
            raise ValueError(f"Пакет {self.package} отсутствует у продукта {self.products}")

class paymant_method(models.Model):
    name = models.CharField(max_length=45)

class receiving_method(models.Model):
    name = models.CharField(max_length=45) 

class point_of_issue(models.Model):
    index = models.CharField(max_length=45)
    sity = models.CharField(max_length=45)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=45)
    
class order(models.Model):
    user = models.OneToOneField(users, on_delete=models.CASCADE)
    final_cost = models.DecimalField(max_digits=7, decimal_places=0)
    order_list = models.ManyToManyField(products, through='orders_list')
    comment = models.TextField()
    payment_method = models.OneToOneField(paymant_method, on_delete=models.CASCADE)
    receiving_method = models.OneToOneField(receiving_method, on_delete=models.CASCADE)
    point_of_issue = models.OneToOneField(point_of_issue, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        final_cost = 0
        for product in orders_list.objects.filter(order = self.id):
            final_cost += getattr(product, 'cost') * getattr(product, 'quantity')
        self.final_cost = final_cost
        super().save(*args, **kwargs)

class orders_list(models.Model):
    cost = models.DecimalField(max_digits=7, decimal_places=0)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    package = models.ForeignKey(package, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        packages = product_has_packages.objects.filter(product=self.product.id)
        flag = False
        for package in packages:
            if self.package == getattr(package, 'package'):
                self.cost = self.package.cost
                flag = True
                break
        if flag:
            super().save(*args, **kwargs)
        else: 
            raise ValueError(f"Пакет {self.package} отсутствует у продукта {self.product}")