from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {'title': 'Рассылки', 'description': 'Рассылки'},
            {'title': 'Телеграм боты', 'description': 'Телеграм боты'},
            {'title': 'Полезные утилиты', 'description': 'Полезные утилиты'},
            {'title': 'Веб-приложения', 'description': 'Веб-приложения'},
            {'title': 'Микросервисы', 'description': 'Микросервисы'}
        ]

        categories_for_create = []

        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)
