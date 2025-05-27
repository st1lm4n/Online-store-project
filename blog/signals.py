from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post


@receiver(post_save, sender=Post)
def send_congratulation_email(sender, instance, **kwargs):
    if instance.views_count >= 100:
        send_mail(
            "Поздравляем!",
            "Ваша статья достигла 100 просмотров!",
            "admin@example.com",
            ["your@email.com"],
            fail_silently=False,
        )
