# coding=utf-8

from django.conf.urls import url
from django.views.generic import DetailView
from .models import Course

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^curso/(?P<slug>[\w_-]+)/$',
        DetailView.as_view(
            model=Course, context_object_name='course'
        ),
        name='course'
    ),
]
