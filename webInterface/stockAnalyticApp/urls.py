__author__ = 'vishnu'
from django.conf.urls import url

from . import views

"""
    Registering all the url concern to this WebApp
"""

urlpatterns = [

    url(r"^$", views.index, name='index'),
    url(r"exchanges/(?P<NAME>\w+)/$", views.exchange, name="exchanges"),

]