from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='phones')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()