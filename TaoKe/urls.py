from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^share/', include('share.urls',namespace='share')),
    url(r'^account/',include('account.urls',namespace='account')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^adminq/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^artTemplate/$',TemplateView.as_view(template_name='demo/artTemplate.html')),
        url(r'^jquery/$',TemplateView.as_view(template_name='jquery.html')),
        url(r'^Bootstrap/$',TemplateView.as_view(template_name='bootstrap/Bootstrap.html')),
        url(r'^test/$',TemplateView.as_view(template_name='test.html')),
        )