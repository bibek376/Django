from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    dept_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    department_id=models.ForeignKey(Department,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department_id=models.ForeignKey(Department,on_delete=models.PROTECT)
    uid=models.CharField(max_length=50,null=False)
    name=models.CharField(max_length=100,null=False)
    dob=models.DateField()

    def __str__(self):
        return self.name