from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_completed", "created_at", "updated_at")
    list_filter = ("is_completed", "created_at")
    search_fields = ("title", "description")
