from email.policy import default
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    profession = models.CharField(max_length = 50)
    telephone = models.PositiveBigIntegerField()
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.name
