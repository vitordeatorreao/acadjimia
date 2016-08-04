# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

class IndexView(FormView):

    template_name = 'index.html'
    form_class = AuthenticationForm

def login_or_redirect(request, *args, **kwargs):
    if (request.user.is_authenticated()):
        return redirect('index')
    else:
        return login(request, *args, **kwargs)

class RegisterUser(CreateView):

    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index')
        else:
            return super(RegisterUser, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super(RegisterUser, self).get_context_data(**kwargs)
        data['register_form'] = data.get('form')
        data['form'] = AuthenticationForm()
        return data
