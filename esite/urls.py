from django.conf.urls import patterns, include, url
from django.contrib import admin

# import catalog.views

urlpatterns = [
#     url(r'^$', catalog.views.home),
    url(r'^store/$', include('store.urls')),

    url(r'^admin/', include(admin.site.urls)),
]


# settings for development environment DEBUG
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
