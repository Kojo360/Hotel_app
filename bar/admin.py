from django.contrib import admin
from .models import BarItem


@admin.register(BarItem)
class BarItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'volume', 'alcohol_content', 'is_available', 'is_featured']
    list_filter = ['category', 'is_available', 'is_featured', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_available', 'is_featured']
    ordering = ['category', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Category & Details', {
            'fields': ('category', 'alcohol_content', 'volume')
        }),
        ('Image', {
            'fields': ('image',),
            'description': "Paste a direct HTTPS image URL instead of uploading files."
        }),
        ('Availability', {
            'fields': ('is_available', 'is_featured')
        }),
    )

