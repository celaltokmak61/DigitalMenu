from django.db import models
from autoslug import AutoSlugField
from PIL import Image
import os
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images', default='noimage.png')
    active = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,  null=True, blank=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.image:
            img_path = os.path.join(settings.STATIC_ROOT, 'noimage.png')
            img = Image.open(img_path)
            output = BytesIO()
            img.convert('RGB').save(output, format='JPEG', quality=100)
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.name, 'image/jpeg', sys.getsizeof(output), None)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
      
class SiteSettings(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='site/logos/', default='site/logos/default.png')

    def __str__(self):
        return self.name
      
