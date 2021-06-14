from django.db import models


#This is for Database work.

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name
        #can create a class with diff. name in admin pannel


class FeedBack(models.Model):
    name=models.CharField(max_length=300)
    post=models.CharField(max_length=300)
    image=models.TextField()
    feedback=models.TextField()

    def __str__(self):
        return self.name