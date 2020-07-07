from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class cart(models.Model):

    price_old = models.IntegerField()
    price_new = models.IntegerField()
    name = models.CharField(max_length=50)
    bookfront_cover = models.ImageField(upload_to='pics',default='picc')
    bookback_cover = models.ImageField(upload_to='pics',default='picc')
    book_index_1 = models.ImageField(upload_to='pics',default='picc')
    book_index_2 = models.ImageField(upload_to='pics',default='picc')
    book_index_3 = models.ImageField(upload_to='pics',default='picc')
    book_index_4 = models.ImageField(upload_to='pics',default='picc')
    hot = models.BooleanField(default=True)
    bestseller = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    owner = models.ForeignKey( User , on_delete=models.CASCADE)
    cart = models.IntegerField()