from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=("title","user","is_deleted","is_completed")
    list_display_links=("title")
    list_filter=("is_deleted","is_completed")
    search_fields=("title","description")
    
