from django.db import models


class Category(models.Model):
    """
    Product categories
    """

    name = models.CharField(
        name="category_name",
        help_text="Stores category name",
        max_length=255
    )

    category_type = models.CharField(
        name='category_type',
        help_text="Stores category type",
        max_length=255
    )

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    Model storing products
    """

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(
        name="product_name",
        help_text="stores product name",
        max_length=255
    )
    product_type = models.CharField(
        name="product_type",
        help_text="stores product type",
        max_length=255
    )
    image = models.URLField(default=None)
    price = models.PositiveIntegerField(name="price")
    desc = models.CharField(
        name="product_desc",
        help_text="stores product name",
        max_length=255
    )
    extra_data = models.TextField(
        name="extra_data",
        help_text="Stores extra data about the product"
    )

    def __str__(self):
        return self.product_name


class CarouselImages(models.Model):
    """
    Model for storing carousel images
    """

    url = models.URLField(name='url')
