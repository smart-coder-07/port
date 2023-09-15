from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    number = models.IntegerField()
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
