from django.contrib import admin

from .models import Template, TemplateVariable

# Register your models here.
class TemplateVariableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
    list_display_links = ('id',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'created_at', 'updated_at'),
        }),
    )

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
    list_display_links = ('id',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('text', 'variables', 'created_at', 'updated_at'),
        }),
    )

admin.site.register(Template, TemplateAdmin)
admin.site.register(TemplateVariable, TemplateVariableAdmin)