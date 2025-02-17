# Create your models here.
from audioop import reverse

from django.contrib.auth.models import User
from django.db import models
from unicodedata import category


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
        category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
        created_by = models.ForeignKey(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=255, default='admin')
        description = models.TextField(blank=True)
        image = models.ImageField(upload_to='images/')
        slug = models.SlugField(max_length=255, unique=True)
        price = models.DecimalField(max_digits=4, decimal_places=2)
        in_stock = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        class Meta:
            verbose_name_plural = 'products'
            ordering = ('-created',)

        def __str__(self):
            return self.title
