# newsapp/apps.py

from django.apps import AppConfig

class NewsappConfig(AppConfig):
    name = 'newsapp'

    def ready(self):
        import newsapp.templatetags.censor

