from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # To use signals in the app we need to import them.
    # The ready is used to intialize the signals when this app is created/started in the main app
    def ready(self):
        import users.signals