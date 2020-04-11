from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from django.contrib.postgres.fields import JSONField
from accounts.constants import GENDER_CHOICES
from myapp.constants import RESPONSE_TYPES_CHOICE, QUESTION_TOPIC_CHOICE


class BaseQuestion(models.Model):
    response_type = models.PositiveSmallIntegerField(
        choices=RESPONSE_TYPES_CHOICE,
        null=True,
        blank=True,
        help_text="hint for what type of response expect from end user",
    )
    topic = models.CharField(
        max_length=225,
        choices=QUESTION_TOPIC_CHOICE,
        blank=True,
        null=True,
        help_text="question topic",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.body[:50]


class Question(models.Model):
    base_question = models.ForeignKey(
        BaseQuestion,
        related_name='questions',
        on_delete=models.CASCADE,
        help_text="the base question it can trace back to, one base question can have multiple version of questions"
    )
    min_age_date = models.DateField(null=True, blank=True, help_text="minimal user birthday filter")
    max_age_date = models.DateField(null=True, blank=True, help_text="maximum user birthday filter")
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True, help_text="user gender filter")
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]


class QuestionChangeHistory(models.Model):
    """
        a model used to track Question/BaseQuestion change history
    """
    base_question = models.ForeignKey(
        BaseQuestion,
        related_name='question_change_histories',
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        Question,
        related_name='question_change_histories',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    before_body = models.TextField()
    after_body = models.TextField()
    diff = JSONField(
        blank=True, null=True, help_text="question text diff"
    )


class Response(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='responses',
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        related_name='responses',
        on_delete=models.CASCADE,
    )
    body = models.CharField(max_length=1024)

    def __str__(self):
        return self.body[:50]
