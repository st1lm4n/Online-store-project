from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product
from blog.models import Post


class Command(BaseCommand):
    help = 'Создает группы и назначает права доступа'

    def handle(self, *args, **options):
        # Группа модераторов
        mod_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получение разрешений
        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(content_type=content_type)

        # Назначение прав модераторам
        unpublish_perm = permissions.get(codename='can_unpublish_product')
        delete_perm = permissions.get(codename='delete_product')
        change_status_perm = permissions.get(codename='can_change_publish_status')

        mod_group.permissions.add(unpublish_perm, delete_perm, change_status_perm)

        # Группа контент-менеджеров (дополнительно)
        content_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        blog_content_type = ContentType.objects.get_for_model(Post)
        blog_permissions = Permission.objects.filter(
            content_type=blog_content_type,
            codename__in=['add_post', 'change_post', 'delete_post', 'view_post']
        )
        custom_perm = Permission.objects.get(
            codename='manage_blog_content',
            content_type=blog_content_type
        )
        content_group.permissions.add(*blog_permissions, custom_perm)

        self.stdout.write(self.style.SUCCESS('Группы и права успешно созданы'))