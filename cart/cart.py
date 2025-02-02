import decimal

from shop.models import ProductProxy


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")

        if not cart:
            cart = self.session["session_key"] = {}

        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductProxy.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = decimal.Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def our_len(self):
        return sum(item["qty"] for item in self.cart.values())

    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "qty": quantity,
                "price": str(product.price),
            }
        self.cart[product_id]["qty"] += quantity

        self.session.modified = True
