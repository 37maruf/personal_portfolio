from .models import Profile


def site_profile(request):
    return {"profile": Profile.objects.first()}
