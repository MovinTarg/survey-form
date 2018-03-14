from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process', views.surveysProcess),
    url(r'^result', views.result),
    url(r'^goBack', views.goBack),
]