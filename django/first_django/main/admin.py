from django.contrib import admin

# Register your models here

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : [ 'question_text']}),
        ("Date Information", {"fields":['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['pub_date', 'question_text', 'was_published_recently']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
