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
    


