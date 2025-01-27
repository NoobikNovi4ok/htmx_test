from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView

from cart.cart import Cart
from shop.models import ProductProxy


class CartView(TemplateView):
    template_name = "cart/cart-view.html"


def cart_add(request):
    cart = Cart(request)

    if request.method == "POST":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        product = get_object_or_404(ProductProxy, id=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_qty = cart.our_len()

        response = JsonResponse({"qty": cart_qty, "product": product.title})

        return response


def cart_delete(request):
    pass


def cart_update(request):
    cart = Cart(request)
