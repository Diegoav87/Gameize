from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Game, GameAdmin)
