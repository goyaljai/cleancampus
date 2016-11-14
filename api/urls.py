from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
import api
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^analysis/',api.index,name = 'anylasis'),
    url(r'^signup/',api.signup,name = 'api-signup'),
    url(r'^complaint/',api.ComplaintView.as_view(),name = 'api-complaint'),
    url(r'^login/', obtain_auth_token, name='api-token'),
    url(r'^profile/',api.get_profile,name = 'api-get'),
    url(r'^getcomplaint/',api.ComplaintView.as_view(),name = 'api-get-complaint'),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)