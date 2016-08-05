from django.shortcuts import render
from django.views.generic import ListView

from .models import Course

# Create your views here.

class IndexView(ListView):

    paginate_by = 3
    context_object_name = 'courses'
    model = Course
    template_name = 'catalog/index.html'
    
