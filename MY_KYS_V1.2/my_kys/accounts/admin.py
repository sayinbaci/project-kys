# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    filter_horizontal = ()  # Boş bırakabilirsiniz
    model = CustomUser
    list_display = ('username', 'email', 'identity_number', 'name', 'surname','phone','birth_date', 'city','is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        ('Kişisel Bilgiler', {'fields': ('email', 'birth_date','password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)