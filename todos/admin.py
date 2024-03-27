from django.contrib import admin
from todos.models import Task
# Register your models here.

class TaskADmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'completed', 'deadline')
    search_fields = ('title', 'body')
    list_filter = ('title', 'important', 'created_at', 'completed')
    list_per_page = 10
    ordering = ('important',)

admin.site.register(Task, TaskADmin)
