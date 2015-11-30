from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
    url(r'^category/(?P<category_id>[0-9]*)/(?P<page>[0-9]*)/$', views.show_category, name='category'),
    url(r'^product/(?P<itemID>[0-9]*)/$', views.show_product, name='product'),
]