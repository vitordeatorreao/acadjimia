# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from catalog.models import Course, Category

from .forms import ContactForm

# Create your views here.

class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data['courses'] = Course.objects.featured()
        return data

def login_or_redirect(request, *args, **kwargs):
    if (request.user.is_authenticated()):
        return redirect('index')
    else:
        login_view = login(request, *args, **kwargs)
        try:
            login_view.context_data['login_form'] = login_view.context_data['form']
        except Exception:
            pass
        return login_view

class RegisterUser(CreateView):

    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index')
        else:
            return super(RegisterUser, self).dispatch(request, *args, **kwargs)

class ContactView(FormView):

    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'

    def form_valid(self, form):
        send_mail(
            'Formulário de Contato',
            form.cleaned_data['message'],
            form.cleaned_data['email'],
            ['a@b.com'],
            fail_silently=False
        )
        return super(ContactView, self).form_valid(form)
