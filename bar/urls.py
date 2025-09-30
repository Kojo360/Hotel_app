from django.urls import path
from . import views

app_name = 'bar'

urlpatterns = [
    path('', views.bar_menu, name='bar_menu'),
]
