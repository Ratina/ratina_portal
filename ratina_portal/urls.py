from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', include(
        'home.urls',
        app_name='home',
        namespace='home',
    )),
    url(r'^blog/', include(
        'blog.urls',
        app_name='blog',
        namespace='blog',
    )),
    url(r'^lang/', include(
        'lang.urls',
        app_name='lang',
        namespace='lang'
    )),
    url(r'^others/', include(
        'others.urls',
        app_name='others',
        namespace='others'
    )),
    url(r'^about/', include(
        'about.urls',
        app_name='about',
        namespace='about'
    )),
    url('^markdown/', include(
        'django_markdown.urls'
    )),
    url(r'^admin/', include(admin.site.urls)),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
