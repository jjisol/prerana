from .models import Instructor, Yoga, VisitingArea, Instrument
from .models import YogaInstructor, PilatesInstructor, VisitingInstructor
from django_filters import FilterSet
from django_filters import ChoiceFilter, ModelMultipleChoiceFilter
from django_filters import ModelChoiceFilter

class YogaFilter(FilterSet):
    gender = ChoiceFilter(choices=Instructor.GENDER_CHOICES)
    style = ModelMultipleChoiceFilter(
        queryset=Yoga.objects.all(),
        field_name='yoga_instructor__style'
    )
    career = ChoiceFilter(choices=YogaInstructor.CAREER_CHOICES,
        field_name='yoga_instructor__career')

    class Meta:
        model = Instructor
        fields = ['gender', 'style', 'career', ]

    def qs(self):
        parent = super().qs
        return parent.filter(yoga_instructor__isnull=False)


class PilatesFilter(FilterSet):
    gender = ChoiceFilter(choices=Instructor.GENDER_CHOICES)
    career = ChoiceFilter(choices=YogaInstructor.CAREER_CHOICES,
        field_name='pilates_instructor__career')

    class Meta:
        model = Instructor
        fields = ['gender', 'career', ]

    def qs(self):
        parent = super().qs
        return parent.filter(pilates_instructor__isnull=False)

class VisitingFilter(FilterSet):
    gender = ChoiceFilter(choices=Instructor.GENDER_CHOICES)
    career = ChoiceFilter(choices=VisitingInstructor.CAREER_CHOICES,
        field_name='visiting_instructor__career')
    visiting_area = ModelMultipleChoiceFilter(
        queryset=VisitingArea.objects.all(),
        field_name='visiting_instructor__visiting_area'
    )
    instrument = ModelMultipleChoiceFilter(
        queryset=Instrument.objects.all(),
        field_name='visiting_instructor__instrument'
    )

    class Meta:
        model = Instructor
        fields = ['gender', 'career', ]

    def qs(self):
        parent = super().qs
        return parent.filter(visiting_instructor__isnull=False )
