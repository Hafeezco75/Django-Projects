import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf import settings


# Create your models here
class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    #slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    inventory = models.PositiveSmallIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField('Promotion', related_name='+')
    #review_set =


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36, default=uuid)
    created_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class Order(models.Model):
    PAYMENT_STATUS = [
        ('P', 'Pending'),
        ('S', 'Success'),
        ('C', 'Canceled'),
    ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default='P')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class Promotion(models.Model):
    product = models.ManyToManyField(Product, related_name='+')
    discount = models.DecimalField(max_digits=6, decimal_places=2)


class Review(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='reviews')
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=100)

