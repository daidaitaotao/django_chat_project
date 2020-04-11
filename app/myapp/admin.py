from django.contrib import admin

# Register your models here.

from myapp.models import BaseQuestion, Question, QuestionChangeHistory, Response


@admin.register(BaseQuestion)
class BaseQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "date_created", "updated_at")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "updated_at")


@admin.register(QuestionChangeHistory)
class QuestionChangeHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "date_created", "base_question", "question")


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "date_created", "question")