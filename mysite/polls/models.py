from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='ques/images', blank=False, null=False)

    def __str__(self):
        return self.name