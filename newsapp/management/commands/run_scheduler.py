from django.core.management.base import BaseCommand
from newsapp.tasks import start  # Импортируем вашу функцию

class Command(BaseCommand):
    help = 'Запуск планировщика задач'

    def handle(self, *args, **options):
        start()  # Запуск планировщика
