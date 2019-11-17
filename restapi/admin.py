# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Quiz, Questions

# Register your models here.
class QestionsInline(admin.StackedInline):
    model=Questions
    extra=3

class QuizAdmin(admin.ModelAdmin):
    list_display=('name','description')

    inlines=[QestionsInline]

admin.site.register(Quiz, QuizAdmin)