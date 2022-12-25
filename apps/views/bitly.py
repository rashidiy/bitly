from random import randint
from string import ascii_lowercase, ascii_uppercase, digits

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.views.generic.detail import BaseDetailView

from apps.models import Link


class MainView(ListView):
    template_name = 'apps/index.html'
    queryset = Link.objects.all()


class CreateShort(CreateView):
    model = Link
    fields = ('long',)
    success_url = reverse_lazy('bitly')
    template_name = 'apps/index.html'

    def form_valid(self, form):
        if self.request.user.is_anonymous:
            return redirect('sign-up')
        characters = ascii_lowercase + ascii_uppercase + digits
        short = ''
        while not short and short not in Link.objects.values_list('short'):
            short = ''.join([characters[randint(0, len(characters))] for _ in range(8)])
        form.instance.user = self.request.user
        form.instance.short = self.request.get_host() + '/ui/' + short
        return super().form_valid(form)


def open_page(request, short):
    short_link = request.get_host() + '/ui/' + short
    link = get_object_or_404(Link, short=short_link)
    return HttpResponseRedirect(link.long)


def page_not_found(request, exception, template_name='apps/404.html'):
    return render(request, template_name)
