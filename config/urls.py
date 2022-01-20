"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('rest_registration.api.urls')),
    path('core/', include(('apps.core.urls', 'apps.core'), namespace='core')),
    path('webhook/', include(('mods.webhook.urls', 'mods.webhook'), namespace='webhook')),
    path('emailcare/', include('apps.emailcare.urls')),
    path('social/', include('apps.social.urls')),
    path('livechat/', include('apps.livechat.urls')),
    path('chatbot/', include('apps.chatbot.urls')),
    path('mixed/', include('apps.mixed.urls')),
    path('reports/', include('apps.reports.urls')),
    path('casex/', include('apps.casex.urls')),
    path('apps/', include('apps.mavrik_apps.urls')),
    path('content/', include('mods.content.urls')),
    path('nlu/', include('mods.nlu.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
