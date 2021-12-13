from django.db import models

# Create your models here.

class AirtimeUser(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.phone_number
