from django.contrib import admin

# Register your models here.

from myapp.models import BaseQuestion, Question, QuestionChangeHistory, Response

admin.site.register(BaseQuestion)
admin.site.register(Question)
admin.site.register(QuestionChangeHistory)
admin.site.register(Response)