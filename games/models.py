from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Game(models.Model):
    STATUS = [
        ('Released', 'Released'),
        ('In Development', 'In Development'),
        ('Early Access', 'Early Access')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    title = models.CharField(max_length=150, unique=True)
    short_description = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    release_status = models.CharField(choices=STATUS, max_length=200)
    developer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='orders', blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, related_name='order_items', blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return self.game.price * self.quantity



