from django.db import models
from django.core.validators import MinValueValidator


class Room(models.Model):
    """Model representing a hotel room"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    amenities = models.TextField(help_text="Enter amenities separated by commas")
    image = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Paste a direct image URL (e.g. Unsplash)"
    )
    is_visible = models.BooleanField(default=True, help_text="Toggle room visibility to customers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_amenities_list(self):
        """Return amenities as a list"""
        return [amenity.strip() for amenity in self.amenities.split(',') if amenity.strip()]

    @property
    def image_url(self) -> str:
        """Return the image URL string (empty if not provided)."""
        return self.image or ""


class Booking(models.Model):
    """Model representing a room booking request"""
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    special_request = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} - {self.room.name} ({self.check_in} to {self.check_out})"
