from django.urls import path
from cart.views import CartView, cart_add, cart_delete, cart_update

app_name = "cart"

urlpatterns = [
    path("", CartView.as_view(), name="cart-view"),
    path("add/", cart_add, name="add-to-cart"),
    path("delete/", cart_delete, name="delete-to-cart"),
    path("update/", cart_update, name="update-to-cart"),
]
