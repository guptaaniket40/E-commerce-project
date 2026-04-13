from django.db import models

# Create your models here.

# PRODUCT
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


# CART
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


# ORDER
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    status = models.CharField(max_length=50, default="pending")


# PAYMENT
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50, default="success")