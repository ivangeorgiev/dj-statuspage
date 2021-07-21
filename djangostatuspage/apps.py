from django.apps import AppConfig


class DjangostatuspageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangostatuspage'
    
    def ready(self):
        from . import signals
