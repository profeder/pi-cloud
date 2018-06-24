from ..models import MenuItem
from django import template


register = template.Library()


@register.simple_tag(name='menu')
def getBuildMenu():
    models=  MenuItem.objects.order_by('super_item_id', 'order')
    items = []
    for item in models:
        if item.super_item_id is None:
            items.append(item)

    return items