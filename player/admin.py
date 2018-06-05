from django.contrib import admin

# Register your models here.
from player.models import Points, Player, Game
admin.site.register(Player)
admin.site.register(Points)
admin.site.register(Game)