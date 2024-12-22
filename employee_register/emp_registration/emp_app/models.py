from django.db import models

# Create your models here.


class Position(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=200)
    emp_code=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    position=models.ForeignKey(Position,on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name