from django.contrib.auth.models import User


def users(request):
    return {
        "users": User.objects.filter(is_active=True),
    }
