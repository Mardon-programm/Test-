from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.phone_number

