from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    url(r'^post/(?P<id>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
