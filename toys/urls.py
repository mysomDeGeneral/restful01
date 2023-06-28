from django.urls import re_path as url
from . import views  

urlpatterns = [
    url(r'^toys/$', views.toy_list),
    url(r'^toys/(?P<pk>[0-9]+)/$', views.toy_detail),
]