from django.db import models

# Create your models here.
class categorydb(models.Model):
    categoryname = models.CharField(max_length=100,null=True,blank=True)
    descrption = models.CharField(max_length=100,null=True,blank=True)
    product_image = models.ImageField(upload_to="product_Images",max_length=100,null=True,blank=True)
class productdb(models.Model):
    category = models.CharField(max_length=100,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    productimage = models.ImageField(upload_to="productimages",null=True,blank=True)
