from django.db import models
from django.core.validators import MinValueValidator


class MenuItem(models.Model):
    """Model representing a restaurant menu item"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    category = models.CharField(
        max_length=100,
        choices=[
            ('appetizer', 'Appetizer'),
            ('main', 'Main Course'),
            ('dessert', 'Dessert'),
            ('beverage', 'Beverage'),
        ],
        default='main'
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} - ${self.price}"
