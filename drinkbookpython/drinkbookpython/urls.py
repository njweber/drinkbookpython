from django.contrib import admin
from django.conf.urls import url

from drinks import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^alldrinks/$', views.alldrinks, name='alldrinks'),
	url(r'^partydrinks/$', views.partydrinks, name='partydrinks'),
	url(r'^findadrink/$', views.findadrink, name='findadrink'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^drinks/(\d+)/', views.drink_detail, name='drink_detail'),
]
