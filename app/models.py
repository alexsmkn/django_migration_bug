# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Parent(models.Model):
    bar = models.IntegerField()


class Side(models.Model):
    baz = models.IntegerField()


# class Child(Parent):
#     foo = models.ForeignKey(Side)


'''
1. Make models Parent, Side and Child
2. Make migration
3. Comment out Child model
4. Make migration
5. Migrate
6. Profit
'''

