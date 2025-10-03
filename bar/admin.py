from django.contrib import admin
from django import forms
from .models import BarItem


class BarItemAdminForm(forms.ModelForm):
    image = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'https://example.com/bar.jpg'}),
        help_text='Paste a direct HTTPS image URL instead of uploading files.'
    )

    class Meta:
        model = BarItem
        fields = '__all__'


@admin.register(BarItem)
class BarItemAdmin(admin.ModelAdmin):
    form = BarItemAdminForm
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

