from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView
from center.models import Center
from instructor.models import Instructor
from onedayclass.models import OnedayClass

def HomePageView(request):
    centers = Center.objects.all().order_by('id')[:8]
    instructors = Instructor.objects.all().order_by('id')[:8]
    classes = OnedayClass.objects.all().order_by('id')[:8]
    return render(request, 'home/home.html'
        , {'centers':centers, 'instructors':instructors, 'classes':classes})
