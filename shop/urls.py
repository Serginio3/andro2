from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    url(r'^about', views.about, name='about'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^$', views.product_list, name='product_list')
]


app_name = 'shop'