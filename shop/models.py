from random import choice
import string
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


def rand_slug():
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
        max_length=250, unique=True, null=False, editable=False, verbose_name="URL"
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

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
