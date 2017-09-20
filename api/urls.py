from django.conf.urls import patterns, include, url
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> a177d5999f5a83979b939e1d664ee4cfe5d63c56
=======
>>>>>>> a177d5999f5a83979b939e1d664ee4cfe5d63c56
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
import api
admin.autodiscover()


urlpatterns = patterns('',
<<<<<<< HEAD
<<<<<<< HEAD
    url(r'^analysis/',api.index,name = 'anylasis'),
=======
	url(r'^analysis/',api.index,name = 'anylasis'),
>>>>>>> a177d5999f5a83979b939e1d664ee4cfe5d63c56
=======
	url(r'^analysis/',api.index,name = 'anylasis'),
>>>>>>> a177d5999f5a83979b939e1d664ee4cfe5d63c56
    url(r'^signup/',api.signup,name = 'api-signup'),
    url(r'^complaint/',api.ComplaintView.as_view(),name = 'api-complaint'),
    url(r'^login/', obtain_auth_token, name='api-token'),
    url(r'^profile/',api.get_profile,name = 'api-get'),
    url(r'^getcomplaint/',api.ComplaintView.as_view(),name = 'api-get-complaint'),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
<<<<<<< HEAD
<<<<<<< HEAD
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a177d5999f5a83979b939e1d664ee4cfe5d63c56
=======
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a177d5999f5a83979b939e1d664ee4cfe5d63c56
