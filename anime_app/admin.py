from django.contrib import admin

from .models import Anime, AnimeMedia, Comments

# Register your models here.
admin.site.register(Anime)
admin.site.register(AnimeMedia)
admin.site.register(Comments)

