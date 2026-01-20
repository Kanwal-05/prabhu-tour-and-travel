from django.apps import AppConfig

class PtatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ptat'

    def ready(self):
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except Exception as e:
            print("DB not ready:", e)
