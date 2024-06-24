from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200,)
    image = models.ImageField(upload_to='ques/images', blank=True, null=True)

    def __str__(self):
        return self.name