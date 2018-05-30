from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^session_words$', views.index),
    url(r'^session_words/add_word$', views.add_words),
    url(r'^session_words/clear$', views.clear)
]