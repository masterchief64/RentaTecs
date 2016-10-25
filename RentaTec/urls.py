from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from propietarios.urls import Propietario
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'RentaTec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^propietarios/', include('propietarios.urls')),
    url(r'^casas/', include('casas.urls')),

]

urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)
