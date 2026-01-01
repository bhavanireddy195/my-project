
from django.contrib import admin
from .models import Profile

# Register Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'specialization')
    search_fields = ('name', 'role', 'specialization')
