from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from django.urls import path


def landing_page(request):
    return HttpResponse("<h1>Mevrik: No Mens Land</h1>", content_type="text/html; charset=utf-8", charset="utf-8")


urlpatterns = [
                  path('', landing_page),
                  path('admin/', admin.site.urls),
                  path('core/', include(('apps.core.urls', 'apps.core'), namespace='core')),
                  path('webhook/', include(('mods.webhook.urls', 'mods.webhook'), namespace='webhook')),
                  path('emailcare/', include('apps.emailcare.urls')),
                  path('social-care/', include('apps.socialcare.urls')),
                  path('live-chat/', include('apps.livechat.urls')),
                  path('chatbot/', include('apps.chatbot.urls')),
                  path('mixed/', include('apps.mixed.urls')),
                  path('reports/', include('apps.reports.urls')),
                  path('casex/', include('apps.casex.urls')),
                  path('content/', include('mods.content.urls')),
                  path('nlu/', include('mods.nlu.urls')),
                  path('queue/', include('mods.queue_service.urls')),
                #   path('__debug__/', include('debug_toolbar.urls')),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
