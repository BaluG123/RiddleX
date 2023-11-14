# admin.py

from django.contrib import admin
from .models import Level

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['level_number', 'math_question', 'riddle_question', 'answer', 'question_orientation']
    search_fields = ['level_number', 'math_question', 'riddle_question']