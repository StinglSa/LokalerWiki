from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lokaler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^entries/', include('entries.urls', namespace="entries")),
    url(r'^admin/', include(admin.site.urls)),
    ('^pages/',include('django.contrib.flatpages.urls')),
)
