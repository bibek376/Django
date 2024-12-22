from django.db import models

# Create your models here.

class my_task(models.Model):
    id=models.AutoField(primary_key=True)
    task_name=models.CharField(max_length=200)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
