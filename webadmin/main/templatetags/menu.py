from ..models import MenuItem, Permission
from django import template
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.context_processors import PermWrapper


register = template.Library()

@register.simple_tag(name='menu')
def getBuildMenu(user, perms):
    items = []
    if user.username != AnonymousUser.username:
        perm = Permission.objects.filter(user=user)
        models = MenuItem.objects.order_by('super_item_id', 'order')
        for item in models:
            if item.super_item_id is None:
                print(user.has_perm(item.permission.codename))
                if user.has_perm(item.permission.codename):
                    items.append(item)
    return items