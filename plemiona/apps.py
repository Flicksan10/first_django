from django.apps import AppConfig


class PlemionaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plemiona'

    def ready(self):
        import plemiona.signals
