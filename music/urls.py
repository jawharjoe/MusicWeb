from django.conf.urls import url
from . import views

urlpatterns = [

    url('^$',views.index,name='index'),
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]