from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Event, EventRegistration

# Customizing the UserAdmin to use CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Register Models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event)
admin.site.register(EventRegistration)
