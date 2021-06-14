from django.db import models

# Create your models here.

WEEK=(('yes','yes'),('no','no'))
LABEL=(('weeklytop','weeklytop'),('trending','trending'),('new','new'),('','default'))
STATUS=(('active','active'),('inactive','inactive'))


#Nav field is eqivalent to category field.
class Nav(models.Model):
    name=models.CharField(max_length=300)
    slug=models.CharField(max_length=200)


    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Picture(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    ping=models.CharField(max_length=20)
    date=models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=200)
    message=models.TextField()
    email=models.CharField(max_length=50)
    subject=models.TextField()

    def __str__(self):
        return self.name

class NewsProduct(models.Model):
    field=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='media')
    recent=models.BooleanField()
    labels=models.CharField(choices=LABEL,max_length=400)
    status=models.CharField(choices=STATUS,max_length=200)
    slug=models.CharField(max_length=200)
    category=models.ForeignKey(Nav,on_delete=models.CASCADE,null=True)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    date=models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Ad(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media')


    def __str__(self):
        return self.title



