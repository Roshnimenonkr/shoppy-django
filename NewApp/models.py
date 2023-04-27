from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Title")
    slug = models.SlugField(max_length=55, verbose_name="Category Slug")
    description = models.TextField(blank=True, verbose_name="Category Description")
    category_image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Category Image")
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    def __str__(self):
        return self.title
    

class Product(models.Model):
      title=models.CharField(max_length=150,verbose_name="product title")
      slug=models.SlugField(max_length=150,verbose_name="product slug")
      short_description=models.TextField(verbose_name="short description")
      detail_description=models.TextField(blank="True",null="True", verbose_name='detail description')
      product_image=models.ImageField(upload_to="product",blank="True",null="True",verbose_name="product image")
      price=models.DecimalField(max_digits=8,decimal_places=2)
      category=models.ForeignKey(Category, verbose_name="product category",on_delete=models.CASCADE)
      is_active=models.BooleanField(verbose_name="is active")
      is_featured=models.BooleanField(verbose_name="is featured")
    #    the ON DELETE CASCADE option to specify whether you want rows deleted in a child table when corresponding 
    # rows are deleted in the parent table


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.user
    @property
    def total_price(self):
        return self.quantity * self.product.price

    #@property is a decorator for methods in a class that gets the value in the method. 
class relatedimage(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    images=models.FileField(upload_to='Relatedimages',null=True)

class contact(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Comments=models.TextField()     


