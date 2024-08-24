import logging
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post, Subscriber

logger = logging.getLogger(__name__)


@receiver(m2m_changed, sender=Post.postCategory.through)
def notify_subscribers(sender, instance, action, **kwargs):
    if action == "post_add":
        categories = instance.postCategory.all()
        logger.debug(f'Categories: {categories}')
        subscribers = Subscriber.objects.filter(category__in=categories).values_list('user__email',
                                                                                     flat=True).distinct()
        logger.debug(f'Subscribers: {subscribers}')

        post_url = f'http://127.0.0.1:8000/news/{instance.id}/'
        message_content = f'Вышел новый пост "{instance.title}". Вы можете прочитать его по ссылке: {post_url}'

        for email in subscribers:
            send_mail(
                subject=f'New post on NewsPortal',
                message=message_content,
                from_email='autotechsupp74@yandex.ru',
                recipient_list=[email]
            )
            logger.debug(f'Sent email to: {email}')
