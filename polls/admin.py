from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInQuestion(admin.TabularInline):
    
    model = Choice
    extra = 2

class QuestionWithChoiceModel(admin.ModelAdmin):

    fieldsets = [
        (
            "Enter your Question", {"fields": [ "question_txt"] }
        ),
        (
            "Enter the Date", {"fields": ["pub_date"] }
        )
    ]
    inlines = [ChoiceInQuestion]
    list_display = ["question_txt", "pub_date"]
    list_filter = ["pub_date"]
    search_fields = ["question_txt"]

admin.site.register(Question, QuestionWithChoiceModel)