from django.contrib import admin
from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
        "slug",
        "created_at",
    )
    readonly_fields = ("created_at",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brand",
        "slug",
        "price",
        "available",
        "created_at",
        "updated_at",
    )
    list_filter = ("available", "created_at", "updated_at")
    ordering = ("title",)
    prepopulated_fields = {"slug": ("title",)}
