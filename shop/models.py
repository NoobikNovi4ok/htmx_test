from random import choice
import string
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


def rand_slug():
    """
    Generate a random slug string.

    This function creates a random string of 3 characters, using lowercase ASCII letters
    and digits. It's typically used for creating unique identifiers or short random parts
    of URLs.

    Returns:
        str: A randomly generated string of 3 characters, consisting of lowercase
             ASCII letters and digits.
    """
    return "".join(choice(string.ascii_lowercase + string.digits) for i in range(3))


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name="Имя")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
        verbose_name="Родительская категория",
    )
    slug = models.SlugField(
        max_length=250,
        unique=True,
        null=False,
        editable=True,
        verbose_name="URL",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        unique_together = ["slug", "parent"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " > ".join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-pickBetter" + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the absolute URL for the category.

        This method generates the URL for the category list view of this category.
        It uses the 'shop:category-list' URL pattern and includes the category's slug
        as an argument.

        Returns:
            str: The absolute URL for the category list view of this category.
        """
        return reverse("shop:category-list", args=[str(self.slug)])


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    title = models.CharField(max_length=250, verbose_name="Название")
    brand = models.CharField(max_length=250, verbose_name="Бренд")
    description = models.TextField(blank=True, verbose_name="Описание")
    slug = models.SlugField(max_length=250, verbose_name="URL")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", default=99.99
    )
    image = models.ImageField(
        upload_to="products/products/%Y/%m/%d", blank=True, verbose_name="Изображение"
    )
    available = models.BooleanField(default=True, verbose_name="Наличие")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[str(self.slug)])


class ProductManager(models.Manager):
    """
    Custom manager for the Product model.

    This manager provides additional methods for querying the Product model.
    """

    def get_queryset(self):
        """
        Returns a QuerySet of available products.

        This method overrides the default get_queryset method to filter out
        products that are not available.

        Returns:
            QuerySet: A QuerySet containing only available products.
        """
        return super(ProductManager, self).get_queryset().filter(available=True)


class ProductProxy(Product):
    objects = ProductManager()

    class Meta:
        proxy = True
