from django.dispatch import receiver
from django.db.models.signals import pre_save
from myapp.models import Question, BaseQuestion, QuestionChangeHistory
from myapp.utils import get_text_diff

@receiver([pre_save], sender=BaseQuestion)
def create_base_question_change_history(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass  # obj is new
    else:
        before_body = obj.body
        after_body = instance.body
        diff = get_text_diff(before_body, after_body)
        QuestionChangeHistory.objects.create(
            before_body=before_body,
            after_body=after_body,
            base_question=obj,
            diff=diff,
        )


@receiver([pre_save], sender=Question)
def create_question_change_history(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass  # obj is new
    else:
        before_body = obj.body
        after_body = instance.body
        diff = get_text_diff(before_body, after_body)
        QuestionChangeHistory.objects.create(
            before_body=before_body,
            after_body=after_body,
            base_question=instance.base_question,
            diff=diff,
        )
