from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class IndexView(FormView):

    template_name = 'index.html'
    form_class = AuthenticationForm
