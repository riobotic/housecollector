from django.db import models
from django.urls import reverse

class Apartment(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('apartments_detail', kwargs={'pk': self.id})

class House(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'house_id': self.id})
