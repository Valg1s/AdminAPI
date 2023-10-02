from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

from app.views import ProductView,ProductsDetail, ProductsOfMonth, ProductsInStock, ProductsInPickup

urlpatterns = [
    re_path(r"^products/$", ProductView.as_view()),
    re_path(r'^products/(?P<pk>[0-9]+)/$', ProductsDetail.as_view()),
    re_path(r'^products/get_prod_of_month$', ProductsOfMonth.as_view()),
    re_path(r'^products/get_prod_in_stock$', ProductsInStock.as_view()),
    re_path(r'^products/get_prod_in_pickup$', ProductsInPickup.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)