from django.db import models

# Create your models here.

class table(models.Model):
    sno= models.AutoField(primary_key=True)
    first= models.CharField(max_length=100)
    last= models.CharField(max_length=100)
    phone= models.IntegerField(max_length=13)
    
    def __str__(self):
        return self.first