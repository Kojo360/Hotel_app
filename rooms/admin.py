from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_visible', 'created_at']
    list_filter = ['is_visible', 'created_at']
    search_fields = ['name', 'description', 'amenities']
    list_editable = ['is_visible']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Details', {
            'fields': ('amenities', 'image', 'is_visible'),
            'description': "Use HTTPS image URLs (e.g. Unsplash) instead of uploading files."
        }),
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'phone', 'check_in', 'check_out', 'submitted_at']
    list_filter = ['check_in', 'check_out', 'submitted_at', 'room']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['submitted_at']
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Guest Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Booking Details', {
            'fields': ('room', 'check_in', 'check_out', 'special_request')
        }),
        ('System Information', {
            'fields': ('submitted_at',)
        }),
    )
