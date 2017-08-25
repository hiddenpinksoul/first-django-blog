# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default= datetime.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = datetime.now()
        self.save()

    def __str__(self):
        return self.title