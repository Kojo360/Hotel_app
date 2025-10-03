from django.db import models
from django.core.validators import MinValueValidator


class BarItem(models.Model):
    """Model representing a bar/beverage item"""
    
    CATEGORY_CHOICES = [
        ('beer', 'Beer'),
        ('wine', 'Wine'),
        ('spirits', 'Spirits & Liquor'),
        ('cocktail', 'Cocktails'),
        ('soft_drink', 'Soft Drinks'),
        ('juice', 'Juices'),
        ('hot_beverage', 'Hot Beverages'),
        ('mocktail', 'Mocktails'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='spirits'
    )
    alcohol_content = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        help_text="e.g., 40% ABV, Non-alcoholic"
    )
    volume = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="e.g., 330ml, 750ml, 1 glass"
    )
    image = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Paste a direct image URL (e.g. Unsplash)"
    )
    is_available = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this item from the bar menu"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Featured items appear prominently on the bar page"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Bar Item'
        verbose_name_plural = 'Bar Items'

    def __str__(self):
        return f"{self.name} - ${self.price}"

    @property
    def image_url(self) -> str:
        """Return the image URL string (empty if not provided)."""
        return self.image or ""

