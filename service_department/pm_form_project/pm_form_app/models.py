from django.db import models

# Create your models here.
class FormData(models.Model):
    model = models.CharField(max_length=100)
    sn = models.CharField(max_length=20)
    temperature = models.IntegerField()
