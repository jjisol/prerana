#instructor/urls.py
from django.urls import path
from . import views
from django_filters.views import FilterView
from .filters import YogaFilter, PilatesFilter, VisitingFilter
from .models import Instructor

urlpatterns = [
    path('instructor_detail/<int:id>/', views.instructor_detail, name='instructor_detail'),
    path('yoga_detail/', views.yoga_detail, name='yoga_detail'),
    path('pilates_detail/', views.pilates_detail, name='pilates_detail'),
    path('yoga_search/', FilterView.as_view(
            filterset_class = YogaFilter,
            template_name = 'view_on_instructors_yoga.html'),
            name = 'yoga_search'),
    path('pilates_search/', FilterView.as_view(
            filterset_class = PilatesFilter,
            template_name = 'view_on_instructors_pilates.html'),
            name = 'pilates_search'),
    path('visiting_search/', FilterView.as_view(
            filterset_class = VisitingFilter,
            template_name = 'visiting_class_instructor.html'),
            name = 'visiting_search'),
]
