from django.db import models

# Create your models here.

class food(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='asset')
    active = models.BooleanField(default=True)
    qty = models.IntegerField(default=1)
