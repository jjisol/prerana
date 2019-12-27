from django.contrib import admin
from .models import Center, CenterReview
# Register your models here.
class CenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'site']
    search_fields = ['name', 'address']

admin.site.register(Center, CenterAdmin)
admin.site.register(CenterReview)
