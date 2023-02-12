from django.apps import AppConfig

# made a class for movie collection configuring from AppConfig
class MovieCollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_collection'