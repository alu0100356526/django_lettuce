from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	 # Prueba usando el fichero de vistas de sample_app
    url(r'^home/', 'staticpages.sample_app.views.home', name="home"),
    url(r'^about/', 'staticpages.sample_app.views.about', name="about"),
    url(r'^contact/', 'staticpages.sample_app.views.contact', name="contact"),
    url(r'^signup/', 'staticpages.sample_app.views.signup', name="signup"),
    url(r'^help/', 'staticpages.sample_app.views.help', name="help"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
