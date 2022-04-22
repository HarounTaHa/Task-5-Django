from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    country = CountryField()
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.email}'


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.FloatField()
    number_available_on_market = models.IntegerField()
    item_description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.item_name},{self.item_price},{self.number_available_on_market}'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.DecimalField(max_digits=10, decimal_places=0)
    tracking_number = models.DecimalField(max_digits=16, decimal_places=0)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order_number},{self.quantity},{self.item}'
