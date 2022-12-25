from django.contrib.auth.models import User

from apps.models import Link


def counts(request):
    return {
        "users_count": User.objects.count(),
        "links_count": Link.objects.count()
    }
