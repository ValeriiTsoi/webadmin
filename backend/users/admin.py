from django.contrib import admin
from .models import UserAccount

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("username", "role_id", "blocked", "created", "updated")
    search_fields = ("username", "description")
    list_filter = ("blocked",)
