from django.apps import AppConfig


class MyGymAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Add this to configuration to prevent crash and allows for customisation
    name = 'my_gym_app'
