from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

from forum.models import Category
from forum.utils import get_category_wise_products, map_category_and_products


def dashboard(request):
    return render(request, 'forum/dashboard.html')


def index(request):
    categories = Category.objects.all().values()
    product_map = get_category_wise_products(categories)

    data = map_category_and_products(categories, product_map)
    return render(
        request,
        'forum/index.html',
        context={'data': data}
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
