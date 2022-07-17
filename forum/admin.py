from django.contrib import admin

from forum.models import Category, Product, CarouselImages


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(CarouselImages)
class CarouselImagesAdmin(admin.ModelAdmin):
    pass
