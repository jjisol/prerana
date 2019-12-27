from django.contrib import admin
from .models import Instructor, YogaInstructor, PilatesInstructor, VisitingInstructor
from .models import Certificate, Yoga, VisitingArea, Instrument
# Register your models here.

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'sns_url']
    list_filter = ('gender', 'center')
    search_fields = ['name']

class YogaInstructorAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'career', 'price']
    list_filter = ('career', 'style')
    search_fields = ['name']

class PilatesInstructorAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'career', 'price']
    list_filter = ('career', )
    search_fields = ['name']

class VisitingInstructorAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'career', 'price']
    list_filter = ('career', 'instrument', 'visiting_area')
    search_fields = ['name']

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(YogaInstructor, YogaInstructorAdmin)
admin.site.register(PilatesInstructor, PilatesInstructorAdmin)
admin.site.register(VisitingInstructor, VisitingInstructorAdmin)
admin.site.register(Certificate)
admin.site.register(Yoga)
admin.site.register(Instrument)
admin.site.register(VisitingArea)
