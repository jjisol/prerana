from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

#class CustomUserAdmin(UserAdmin):
#    model = CustomUser
#    add_form = CustomUserCreationForm
#    form = CustomUserChangeForm

#admin.site.register(CustomUser, CustomUserAdmin)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'instructor', ]
    search_fields = ['groups',]

admin.site.register(CustomUser, CustomUserAdmin)
