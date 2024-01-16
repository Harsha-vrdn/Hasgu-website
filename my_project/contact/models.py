from django.db import models


# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.TextField()
    timeStamp = models.DateField(auto_now_add=True, blank=True)
