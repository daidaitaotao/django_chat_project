from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from myapp.serializers import QuestionChangeHistorySerializer, BaseQuestionSerializer, QuestionSerializer
from rest_framework import permissions
from rest_framework.response import Response
from myapp.models import QuestionChangeHistory, BaseQuestion, Question
from rest_framework import status
from mysite.exceptions import PermissionError

# Create your views here.


def index(request):
    return HttpResponse("Hello, world.")


class QuestionChangeHistoryView(generics.ListAPIView):
    """
        API endpoint that allows users to view question change history
    """
    serializer_class = QuestionChangeHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        question_id = self.request.query_params.get("question")
        base_question_id = self.request.query_params.get("base_question")
        queryset = QuestionChangeHistory.objects.all()
        if base_question_id:
            queryset = queryset.filter(base_question_id=base_question_id)

        if question_id:
            queryset = queryset.filter(question_id=question_id)

        return queryset

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            records = self.get_queryset()
        else:
            records = QuestionChangeHistory.objects.none()

        serializer = self.serializer_class(records, many=True, context=self.get_serializer_context())
        res = serializer.data
        return Response(res)


class BaseQuestionListCreateView(generics.ListCreateAPIView):
    """
        API endpoint that allows users to view and create base question
    """
    serializer_class = BaseQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        topic = self.request.query_params.get("topic")
        queryset = BaseQuestion.objects.all()
        if topic:
            queryset = queryset.filter(base_question_topic=topic)
        return queryset

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            records = self.get_queryset()
        else:
            records = BaseQuestionSerializer.objects.none()
        serializer = self.serializer_class(records, many=True, context=self.get_serializer_context())
        res = serializer.data
        return Response(res)

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionError

        post = request.data.copy()
        serializer = self.serializer_class(
            data=post, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionListCreateView(generics.ListCreateAPIView):
    """
        API endpoint that allows users to view and create question
    """
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        base_question_id = self.request.query_params.get("base_question")
        topic = self.request.query_params.get("topic")
        queryset = Question.objects.all()
        if base_question_id:
            queryset = queryset.filter(base_question_id=base_question_id)
        if topic:
            queryset = queryset.filter(base_question_topic=topic)

        return queryset

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            records = self.get_queryset()
        else:
            records = Question.objects.none()
        serializer = self.serializer_class(records, many=True, context=self.get_serializer_context())
        res = serializer.data
        return Response(res)

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionError

        post = request.data.copy()
        serializer = self.serializer_class(
            data=post, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)