from django.contrib import admin
from django.utils.html import format_html
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'completed', 'status_badge', 'created_at', 'updated_at')  # ✅ "completed" qo‘shildi
    list_filter = ('priority', 'completed', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('priority', 'completed')  # ✅ Endi ishlaydi
    readonly_fields = ('created_at', 'updated_at', 'status_badge')

    fieldsets = (
        ("Basic Information", {
            'fields': ('title', 'description', 'priority', 'completed', 'status_badge')
        }),
        ("Advanced Options", {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def status_badge(self, obj):
        color = "green" if obj.completed else "red"
        text = "✔ Completed" if obj.completed else "⏳ Active"
        return format_html(f'<span style="background-color:{color}; color:white; padding:4px 8px; border-radius:4px;">{text}</span>')

    status_badge.short_description = "Status"
