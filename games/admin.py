from django.contrib import admin
from .models import Game, Order, OrderItem

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Game, GameAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
