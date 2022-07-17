from collections import defaultdict
from copy import deepcopy

from forum.models import Product


def get_category_wise_products(categories, limit=4):
    """
    Returns products category wise
    """

    product_map = defaultdict(list)
    for category in categories:
        products = Product.objects.filter(
            category_id=category.get('id')
        ).order_by('id').values()
        product_map.update({
            category.get('category_name'): products[:limit]
        })

    return product_map


def map_category_and_products(categories, product_map):
    """
    Maps categories and products
    """

    data = deepcopy(categories)
    for category in data:
        category.update({
            'products': product_map.get(category.get('category_name'), [])
        })

    return data
