from django.core.management.base import BaseCommand
from myapp.models import BaseQuestion


class Command(BaseCommand):
    help = 'Create a base question'

    def add_arguments(self, parser):
        parser.add_argument('body', type=str, help='question body')
        parser.add_argument('topic', type=str,
                            help='question topic, choices: greeting, information, investigation, general')
        # Optional argument
        parser.add_argument('-rt', '--response_type', type=int,
                            help='expected response type, choices: 1 = integer, 2 = text, 3 = boolean')

    def handle(self, *args, **kwargs):
        body = kwargs['body']
        topic = kwargs['topic']
        response_type = kwargs['response_type']
        record = BaseQuestion.objects.create(body=body, topic=topic, response_type=response_type)

        print(f"base question {record.id} has been created")
