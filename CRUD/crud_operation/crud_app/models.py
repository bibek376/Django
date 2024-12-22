from django.db import models

# Create your models here.

class Info_Model(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.TextField()
    description=models.CharField()

    def __str__(self):
        return self.title


