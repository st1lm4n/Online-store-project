from django.core.files import File
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загрузка тестовых данных"

    def handle(self, *args, **options):
        # Удаление старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        category1 = Category.objects.create(
            name="Тестовая категория 1", description="Описание 1"
        )
        category2 = Category.objects.create(
            name="Тестовая категория 2", description="Описание 2"
        )

        # Создание продуктов
        Product.objects.create(name="Тестовый продукт 1", price=100, category=category1)
        Product.objects.create(name="Тестовый продукт 2", price=200, category=category2)

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены!"))
