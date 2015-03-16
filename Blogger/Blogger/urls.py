from django.conf.urls import url, include
from Blogger.router import SharedAPIRootRouter
from django.conf import settings


def api_urls():
    from importlib import import_module
    for app in settings.INSTALLED_APPS:
        try:
            import_module(app + '.urls')
        except (ImportError, AttributeError):
            pass
    return SharedAPIRootRouter.shared_router.urls


urlpatterns = [
    url(r'^', include(api_urls())),
]
