from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SurveySerializer, QuestionSerializer, SurveyEditOrDestroySerializer
from .models import Survey, Question, PassedSurveys
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from datetime import date


class SurveyCreate(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [IsAdminUser]


class SurveyEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveyEditOrDestroySerializer
    permission_classes = [IsAdminUser]


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class QuestionEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class SurveyList(generics.ListAPIView):
    queryset = Survey.objects.filter(date_finish__gte=date.today(), date_start__lte=date.today())
    serializer_class = SurveySerializer


class PassingSurveyCreate(APIView):
    def get(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        serializer = SurveySerializer(survey)
        if not PassedSurveys.objects.get(user=request.user):
            PassedSurveys.objects.create(user=request.user)
        return Response(serializer.data)

    def post(self, request, pk):
        survey = get_object_or_404(Survey, pk=pk)
        passed_survey = PassedSurveys.objects.get(user=request.user)
        passed_survey.surveys.add(survey)
        surveys = passed_survey.surveys.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)


class AllPassedSurveys(generics.ListAPIView):
    def get_queryset(self):
        passed_survey = PassedSurveys.objects.get(user=self.request.user)
        return passed_survey.surveys.all()
    serializer_class = SurveySerializer
