from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin

# AdminPanel Config

UserAdmin.fieldsets [2][1]['fields'] = (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_author",
                    "special_user",
                    "groups",
                    "user_permissions",
)

UserAdmin.list_display += ("is_author" , "special_user")

admin.site.register(Admin, UserAdmin)
