from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SurveyEdit, SurveyCreate, QuestionCreate, QuestionEdit, SurveyList, PassingSurveyCreate, \
    AllPassedSurveys

urlpatterns = [
    path('survey_create/', SurveyCreate.as_view()),
    path('survey_edit/<int:pk>/', SurveyEdit.as_view()),
    path('question_create/', QuestionCreate.as_view()),
    path('question_edit/<int:pk>/', QuestionEdit.as_view()),
    path('survey_list/', SurveyList.as_view()),
    path('pass_survey/<int:pk>', PassingSurveyCreate.as_view()),
    path('all_passed_surveys/', AllPassedSurveys.as_view())
]
