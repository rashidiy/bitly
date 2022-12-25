from django.urls import path
from .views import AuthSignUpView, AuthSignInView

urlpatterns = [
    path('sign-up', AuthSignUpView.as_view(), name='sign-up'),
    path('sign-in', AuthSignInView.as_view(), name='sign-in'),
]
