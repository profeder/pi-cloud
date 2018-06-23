# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pi(models.Model):

    def __init__(self):
        self.__ip = '192.168.1.1'