from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import AuthSignUpView, AuthSignInView, MainView, CreateShort, open_page

urlpatterns = [
    path('sign-up', AuthSignUpView.as_view(), name='sign-up'),
    path('sign-in', AuthSignInView.as_view(), name='sign-in'),
    path('sign-out', LogoutView.as_view(next_page=reverse_lazy('sign-in')), name='sign-out'),

    path('', MainView.as_view(), name='bitly'),
    path('make-short', CreateShort.as_view(), name='make-short'),
    path('ui/<str:short>', open_page, name='open-short'),
]
