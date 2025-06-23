from django.core.cache import cache
from catalog.models import Product, Category
from django.conf import settings

def get_products_by_category_id(category_id):
    if settings.CACHE_ENABLED:
        key = f'products_category_{category_id}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__id=category_id)
            cache.set(key, products, 60 * 15)
        return products
    return Product.objects.filter(category__id=category_id)


def get_cached_products():
    if settings.CACHE_ENABLED:
        key = 'all_products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all().select_related('category')
            cache.set(key, products, 60 * 15)  # Кеш 15 минут
        return products
    return Product.objects.all()