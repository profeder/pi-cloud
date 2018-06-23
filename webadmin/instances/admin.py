from django.contrib import admin
from .models import ComputeInstance, Credential

admin.site.register(ComputeInstance)
admin.site.register(Credential)
