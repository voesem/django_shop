from django.conf import settings
from django.core.mail import send_mail


def send_notification_email_message():
    send_mail(
        "Уведомление",
        "Ваш пост набрал 100 просмотров!",
        settings.EMAIL_HOST_USER,
        ["voesem@yandex.ru"],
        fail_silently=False,
    )
