"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path('accounts/', include('accounts.urls')),
    path('gpt_response/', include('gpt_response.urls')),
    path('game2/', include('game2.urls')),
    path('faceid/', include('faceid.urls')),
]

# urlpatterns = i18n_patterns(
#     path('admin/', admin.site.urls),
#     path("", include("home.urls")),
#     path('accounts/', include('accounts.urls')),
#     path('gpt_response/', include('gpt_response.urls')),
#     path('game2/', include('game2.urls')),
#     path('faceid/', include('faceid.urls')),
# )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)