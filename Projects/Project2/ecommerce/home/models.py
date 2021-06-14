from django.db import models
STOCK=(('In Stock','In Stock'),('Out of Stock','Out of Stock'))
LABELS=(('new','new'),('hot','hot'),('sale','sale'),('defult','default'))
STATUS=(('active','active'),('inactive','inactive'))
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media',null=True)
    status=models.CharField(choices=STATUS,max_length=200,default='inactive')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    slug=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    title=models.CharField(max_length=300)
    price=models.IntegerField()
    discouted_price=models.IntegerField()
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    brand=models.CharField(max_length=200,blank=True)
    stock=models.CharField(choices=STOCK,max_length=100)
    labels=models.CharField(choices=LABELS,max_length=100)
    status=models.CharField(choices=STATUS,max_length=200,null=True)
    image=models.ImageField(upload_to='media',null=True)
    slag=models.CharField(max_length=200,null=True)#should be unique..

    def __str__(self):
        return self.title


class Slider(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    rank=models.IntegerField()
    status=models.CharField(choices=STATUS,max_length=100)
    description=models.TextField()


    def __str__(self):
        return self.title


class Ad(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    rank=models.IntegerField()
    status=models.CharField(choices=STATUS,max_length=100)
    description=models.TextField()


    def __str__(self):
        return self.title