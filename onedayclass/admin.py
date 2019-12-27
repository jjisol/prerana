from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import OnedayClass
# Register your models here.

class OnedayClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date',
     'place', 'price']
    list_filter = [('start_date', DateRangeFilter),
        ('end_date', DateRangeFilter),]
    search_fields = ['name']

admin.site.register(OnedayClass, OnedayClassAdmin)
