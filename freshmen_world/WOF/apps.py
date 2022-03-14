from django.apps import AppConfig


class WofConfig(AppConfig):
    name = 'WOF'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WOF'

    def ready(self):
        import signals