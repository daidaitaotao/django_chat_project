from myapp.models import QuestionChangeHistory, BaseQuestion, Question
from rest_framework import serializers


class QuestionChangeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChangeHistory
        fields = (
            'base_question',
            'question',
            'date_created',
            'before_body',
            'after_body',
            'diff'
        )


class BaseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseQuestion
        fields = (
            'response_type',
            'body',
            'date_created',
            'updated_at',
        )
        read_only_fields = ('date_created', 'updated_at',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'base_question',
            'min_age_date',
            'max_age_date',
            'gender',
            'body',
            'date_created',
            'updated_at',
        )
        read_only_fields = ('date_created', 'updated_at',)