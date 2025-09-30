from django.db import models


class Complaint(models.Model):
    """Model representing a customer complaint"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Complaint from {self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"
