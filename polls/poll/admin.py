from django.contrib import admin
from .models import *

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text']
    list_display_links = ['text']
    inlines = [
        ChoiceInline
    ]
