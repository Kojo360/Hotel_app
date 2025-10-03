from django.contrib import admin
from django import forms
from .models import MenuItem


class MenuItemAdminForm(forms.ModelForm):
    image = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com/menu.jpg'}),
        help_text='Provide a direct HTTPS image URL for menu photos.'
    )

    class Meta:
        model = MenuItem
        fields = '__all__'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemAdminForm
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
            'fields': ('image', 'is_available'),
            'description': "Provide a direct HTTPS image URL for menu photos."
        }),
    )
