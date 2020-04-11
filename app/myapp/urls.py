from django.urls import path
from myapp import views
from django.conf.urls import url


app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    url(r"^question-change-history/$", views.QuestionChangeHistoryView.as_view(), name="question_change_history"),
    url(r"^question/$", views.QuestionListCreateView.as_view(), name="question_list_create"),
    url(r"^base-question/$", views.BaseQuestionListCreateView.as_view(), name="base_question_list_create")
]
