from django.apps import AppConfig


class AboutUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_us'

    def ready(self):
        import about_us.signals
