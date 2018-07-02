from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^log/', views.gateway_login, name='loggings'),
    url(r'^gen/', views.generate_ticket, name='ticketings'),
    ]
