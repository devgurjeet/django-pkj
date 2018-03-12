from django.conf.urls import include, url
from bbm.views import index

urlpatterns = [
   url(r'^$', index, name='index'),
]