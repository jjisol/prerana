from django.shortcuts import render, get_object_or_404
from .models import Instructor
from .filters import YogaFilter, PilatesFilter,VisitingFilter
# Create your views here.
def instructor_detail(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    return render(request, 'instructor_detail.html', {'instructor':instructor})

def yoga_detail(request):
    return render(request, 'yoga_detail.html', {})

def pilates_detail(request):
    return render(request, 'pilates_detail.html', {})

def yoga_search(request):
    instructor_list = Instructor.objects.all()
    yoga_filter = YogaFilter(request.GET, queryset=instructor_list)
    return render(request, 'view_on_instructors_yoga.html', {'filter':yoga_filter})

def pilates_search(request):
    instructor_list = Instructor.objects.all()
    pilates_filter = PilatesFilter(request.GET, queryset=instructor_list)
    return render(request, 'view_on_instructors_pilates.html', {'filter':pilates_filter})

def visiting_class_instructor(request):
    instructors = Instructor.objects.all()
    visiting_filter = VisitingFilter(request.GET, queryset=instructor_list)
    return render(request, 'visiting_class_instructor.html', {'filter':visiting_filter})
