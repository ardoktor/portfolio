from django.conf import settings


def site(request):
    """Absolute URLs for the meta tags in base.html.

    Built from SITE_URL and request.path rather than
    request.build_absolute_uri(): Render terminates TLS and forwards plain
    HTTP, so the request's own scheme cannot be trusted, and path drops the
    query string — otherwise a link shared with ?utm_source=... would
    advertise a different canonical URL than the same page shared without it.
    """
    return {
        'site_url': settings.SITE_URL,
        'canonical_url': f"{settings.SITE_URL}{request.path}",
    }
