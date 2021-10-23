from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ('id',)
    list_display = ['name', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    list_display_links = ('name', 'email',)
    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': ('email', 'password', 'password2')
         }),
    )


admin.site.register(User, UserAdmin)
