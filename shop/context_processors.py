from shop.models import Category


def categories(request):
    all_categories = Category.objects.filter(parent=None)
    return {"categories": all_categories}
