from django.core.cache import cache
from django.conf import settings

from catalog.models import Product


def get_cached_products():
    if settings.CACHE_ENABLED:
        key = 'all_products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all().select_related('category')
            cache.set(key, products, 60 * 15)  # Кеш 15 минут
        return products
    return Product.objects.all()