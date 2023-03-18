from django.contrib import admin
from .models import Developer
from django.contrib.auth.admin import UserAdmin
from .forms import DevChangeForm ,DevCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class DevAdmin(UserAdmin):
    add_form = DevCreationForm
    form = DevChangeForm
    
    model = Developer
    list_display = ['email','role','price','experience','education','summary','is_staff','is_active']
    list_filter = ['email','role','price','is_staff','is_active']
    fieldsets = (
        (None,{'fields':('email','password')}),
        (_("Personal info"), {"fields": (
            "name",
            'mobile',
            'profile',
            'role',
            'skills',
            'experience',
            'p_role',
            'p_company',
            'portfolio_link',
            'price',
            'education',
            'work_mode',
            'summary',
                            )}),
        ('Permissions',{'fields':('is_staff','is_active')}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
admin.site.register(Developer,DevAdmin)    