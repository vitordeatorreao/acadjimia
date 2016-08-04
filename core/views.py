from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class IndexView(FormView):

    template_name = 'index.html'
    form_class = AuthenticationForm

def login_or_redirect(request, *args, **kwargs):
    if (request.user.is_authenticated()):
        return redirect('index')
    else:
        return login(request, *args, **kwargs)
