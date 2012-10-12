from django.conf.urls import patterns, include, url
from DMS.views import home,logoutPage,uploadPage,downloadPage
import os.path
site_media = os.path.join(os.path.dirname(__file__), 'site_media')
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$',home),
     url(r'^login/$','django.contrib.auth.views.login'),
     url(r'^logout/$',logoutPage),
     url(r'^upload/$',uploadPage),
     url(r'^documents/(?P<username>.*)/(?P<downloadfile>.*)/$',downloadPage),
     url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': site_media }),
    # url(r'^pyDMS/', include('pyDMS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
