from django.shortcuts import render, get_object_or_404
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
