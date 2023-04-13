from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('adhaar','firstname','lastname', 'get_full_name','mobile','dob','created_at')
    search_fields = ('username','email','firebase_user_id', 'emailid')
