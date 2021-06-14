from django.db import models
from django.shortcuts import reverse

# Create your models here.

STOCK=(('In Stock','In Stock'),('Out Of Stock','Out Of Stock'))
LABELS=(('new','new'),('hot','hot'),('','default'))
STATUS=(('active','active'),('inactive','inactive'))



class Category(models.Model):
    name=models.CharField(max_length=200)   
    slug=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    status=models.CharField(choices=STATUS,max_length=200,default='inactive')

    def __str__(self):
        return self.name




class SubCategory(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    slug=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    def get_subcat_url(self):
        return reverse("home:subcat",kwargs= {'slug': self.slug})

    

class Item(models.Model):
    title=models.CharField(max_length=300)
    price=models.IntegerField()
    discouted_price=models.IntegerField()
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand=models.CharField(max_length=200,blank=True)
    stock=models.CharField(choices=STOCK,max_length=100)
    labels=models.CharField(choices=LABELS,max_length=100)
    status=models.CharField(choices=STATUS,max_length=200)
    image=models.ImageField(upload_to='media')
    slag=models.CharField(max_length=200,unique=True)#should be unique..
    offer=models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_item_url(self):
        return reverse("home:products",kwargs= {'slug': self.slag})
    def add_to_cart_url(self):
        return reverse("home:add-to-cart",kwargs= {'slug': self.slag})


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

class Cart(models.Model):
    user=models.CharField(max_length=300)
    slug=models.CharField(max_length=200,blank=True)# after onetime makemigration we have to add blank=True.
    product=models.ForeignKey(Item,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1)
    checkout=models.BooleanField(default=False)

    def __str__(self):
        return self.user