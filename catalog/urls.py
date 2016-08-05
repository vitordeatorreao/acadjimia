# coding=utf-8

from django.conf.urls import url
from django.views.generic import DetailView
from .models import Course

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^curso/(?P<slug>[\w_-]+)/$',
        DetailView.as_view(
            model=Course,
            context_object_name='course',
            template_name='catalog/course.html'
        ),
        name='course'
    ),
    url(r'^curso/(?P<slug>[\w_-]+)/inscrever/$', views.enroll, name='enroll'),
    url(
        r'^categoria/(?P<slug>[\w_-]+)/$',
        views.CategoryView.as_view(),
        name='category'
    ),
]
