from django.apps import AppConfig


class TodosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todos'
class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app'

    def ready(self):
        import your_app.signals