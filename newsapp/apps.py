from django.apps import AppConfig

class NewsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsapp'

    def ready(self):
        from .tasks import start_scheduler
        start_scheduler()
        import newsapp.signals