from django.db import models
from django.contrib.auth.models import Permission


class MenuItem(models.Model):
    item = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    super_item = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)

