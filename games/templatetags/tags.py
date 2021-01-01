from django import template
register = template.Library()
from games.models import Order

@register.simple_tag
def current_order_items(request):
    item_order_count = 0

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()
        for item in items:
            item_order_count += item.quantity

    return item_order_count