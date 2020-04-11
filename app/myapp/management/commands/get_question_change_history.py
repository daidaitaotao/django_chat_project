from django.core.management.base import BaseCommand
from myapp.models import QuestionChangeHistory
from myapp.serializers import QuestionChangeHistorySerializer


class Command(BaseCommand):
    help = 'Retrieve a question change history'

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument('-q_id', '--question_id', type=int, help='question id for lookup')
        parser.add_argument('-bq_id', '--base_question_id', type=int, help='base question id for lookup')

    def handle(self, *args, **kwargs):
        base_question_id = kwargs['base_question_id']
        question_id = kwargs['question_id']
        if not base_question_id and not question_id:
            print("cannot find any change history, "
                  "please make sure provide at least one question_id or base_question_id")

        queryset = QuestionChangeHistory.objects.all()
        if base_question_id:
            queryset = queryset.filter(base_question_id=base_question_id)
        if question_id:
            queryset = queryset.filter(question_id=question_id)

        response = QuestionChangeHistorySerializer(queryset, many=True).data
        print(response)