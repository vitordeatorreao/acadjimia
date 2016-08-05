# coding=utf-8

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Course, Category

# Create your views here.

class IndexView(ListView):

    paginate_by = 3
    context_object_name = 'courses'
    model = Course
    template_name = 'catalog/index.html'

class CategoryView(IndexView):

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        courses = Course.objects.filter(category=category)
        return courses

    def get_context_data(self, **kwargs):
        data = super(CategoryView, self).get_context_data(**kwargs)
        data['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return data

def enroll(request, slug):
    if request.user.is_authenticated():
        course = get_object_or_404(Course, slug=slug)
        if request.user in course.enrolled.all():
            messages.warning(
                request,
                "Você já está inscrito no curso %s." % (course.name)
            )
        else:
            course.enrolled.add(request.user)
            messages.success(
                request,
                "Você se inscreveu no curso %s com sucesso." % (course.name)
            )
        return redirect('catalog:course', slug=slug)
    else:
        return redirect('catalog:course', slug=slug)
