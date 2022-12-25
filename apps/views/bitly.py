from django.views.generic import ListView

from apps.models import Bit


class MainView(ListView):
    template_name = 'apps/index.html'
    queryset = Bit.objects.all()
