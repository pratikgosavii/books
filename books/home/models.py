from django.db import models

# Create your models here.


class books(models.Model):

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    dec = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    pattern = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    bookfront_cover = models.ImageField(upload_to='pics',default='picc')
    bookback_cover = models.ImageField(upload_to='pics',default='picc')
    index_1 = models.ImageField(upload_to='pics',default='picc')
    index_2 = models.ImageField(upload_to='pics',default='picc')
    index_3 = models.ImageField(upload_to='pics',default='picc')
    index_4 = models.ImageField(upload_to='pics',default='picc')




    def __str__(self):
        return self.name
