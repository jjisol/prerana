#class/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('class_detail/<int:id>/', views.class_detail, name='class_detail'),
    path('oneday_class_detail/', views.oneday_class_detail, name='oneday_class_detail'),
    url(r'^onedayclass/(?P<id>\d+)/review/$', views.add_review_to_class, name='add_review_to_onedayclass'),
    url(r'^onedayclass/(?P<id>\d+)/remove/$', views.review_remove, name='review_remove'),

]
