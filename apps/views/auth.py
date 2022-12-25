from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.forms import AuthSignUpForm


class AuthSignUpView(FormView):
    form_class = AuthSignUpForm
    template_name = 'apps/sign-up.html'
    success_url = reverse_lazy('sign-up')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AuthSignInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'apps/sign-in.html'
    next_page = reverse_lazy('sign-in')