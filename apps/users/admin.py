from django.contrib import admin

from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_name', 'last_name', 'email', 'mobile_no', 'created_at', 'updated_at')
    ordering = ('-updated_at', )
    list_display_links = ('id', )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'first_name', 'last_name', 'email', 'mobile_no', 'created_at', 'updated_at'),
        }),
    )

admin.site.register(User, UserAdmin)