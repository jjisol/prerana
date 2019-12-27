#center/urls.py
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('center_detail/<int:id>/', views.center_detail, name='center_detail'),
    url(r'^center/(?P<id>\d+)/review/$', views.add_review_to_center, name='add_review_to_center'),
    url(r'^review/(?P<id>\d+)/remove/$', views.review_remove, name='review_remove'),

]
