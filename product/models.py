# models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_list')

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag_list')

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('manufacturer_list')

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ' - ' + self.category.name

    def __repr__(self):
        return self.name + ' - ' + self.category.name