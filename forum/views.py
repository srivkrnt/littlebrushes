from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

from forum.models import Category, Product, CarouselImages
from forum.utils import get_category_wise_products, map_category_and_products


def index(request):
    categories = Category.objects.all().values()
    product_map = get_category_wise_products(categories)
    carousel_images = CarouselImages.objects.all().values()

    data = map_category_and_products(categories, product_map)
    return render(
        request,
        'forum/index.html',
        context={
            'data': data,
            'images': carousel_images
        }
    )


def product_list(request, category_id):
    category = Category.objects.filter(id=category_id).values().first()
    products = Product.objects.filter(category_id=category_id).values()

    return render(
        request,
        'forum/product_list.html',
        context={
            'products': products,
            'category_name': category.get('category_name')
        }
    )


def product_detail(request, product_id):
    product = Product.objects.filter(id=product_id).values().first()

    return render(
        request,
        'forum/product_detail.html',
        context={
            'product': product
        }
    )


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('dashboard')

    else:
        form = UserRegistrationForm()
    return render(request, 'forum/register.html', {'form': form})
