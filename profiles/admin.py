from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"username": ("full_name",)}
    list_display = ["full_name", "username", "email"]
