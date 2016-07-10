from django.contrib import admin

from .models import Reminder, AlertMethod

# Register your models here.

class AlertMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
    list_display_links = ('id',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('type', 'created_at', 'updated_at'),
        }),
    )

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'alert_at', 'message', 'created_at', 'updated_at')
    ordering = ('-updated_at', )
    list_display_links = ('id', )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'alert_at', 'template', 'message', 'method', 'created_at', 'updated_at'),
        }),
    )

admin.site.register(AlertMethod, AlertMethodAdmin)
admin.site.register(Reminder, ReminderAdmin)