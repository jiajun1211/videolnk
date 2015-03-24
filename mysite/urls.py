from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('pinax.blog.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
