from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from shop.models import Category, ProductProxy


def products_view(request):
    products = ProductProxy.objects.all()
    return render(request, "shop/products.html", {"products": products})


class ProductsDetailView(DetailView):
    model = ProductProxy
    context_object_name = "product"
    template_name = "shop/product_detail.html"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, slug=self.kwargs.get(self.slug_url_kwarg))


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = ProductProxy.objects.select_related("category").filter(category=category)
    context = {
        "category": category,
        "products": products,
    }
    return render(request, "shop/category_list.html", context)
