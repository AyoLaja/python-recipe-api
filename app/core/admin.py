from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _

# Register your models here.
class UserAdmin(BaseUserAdmin):
  ordering = ['id']
  list_display = ['email', 'name']
  fieldset = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal Info'), {'fields': ('name',)}),
    (
      _('Permissions'), 
      {'fields': ('is_active', 'is_staff', 'is_superuser')}
    ),
    (_('Important dates'), {'fields': ('last_login',)})
  )

# Register UserAdmin class to User model
admin.site.register(models.User, UserAdmin)