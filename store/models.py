from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    fullName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, default='')
    email = models.EmailField(max_length=100, unique=True, default='')
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.fullName
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default='', blank=True)
    price = models.DecimalField(default=0,max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)
    
    def __str__(self):
        return self.product
