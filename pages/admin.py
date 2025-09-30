from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at', 'is_resolved']
    list_filter = ['is_resolved', 'submitted_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_resolved']
    readonly_fields = ['submitted_at']
    ordering = ['-submitted_at']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Complaint Details', {
            'fields': ('message', 'submitted_at', 'is_resolved')
        }),
    )
