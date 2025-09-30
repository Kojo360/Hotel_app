from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_available']
    ordering = ['category', 'name']
    
    fieldsets = (
        ('Item Information', {
            'fields': ('name', 'description', 'category', 'price')
        }),
        ('Display Settings', {
            'fields': ('image', 'is_available')
        }),
    )
