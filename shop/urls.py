from django.urls import path
from shop.views import (
    products_view,
    category_list,
    ProductsDetailView,
)

app_name = "shop"

urlpatterns = [
    path("", products_view, name="products"),
    path("<slug:slug>", ProductsDetailView.as_view(), name="product-detail"),
    path("search/<slug:slug>", category_list, name="category-list"),
]
