from django.core.cache import cache
from catalog.models import Product, Category
from django.conf import settings

def get_products_by_category(category_slug):
    if settings.CACHE_ENABLED:
        key = f'products_category_{category_slug}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(
                category__slug=category_slug
            ).select_related('category')
            cache.set(key, products, 60 * 15)  # Кеш 15 минут
        return products
    return Product.objects.filter(category__slug=category_slug)