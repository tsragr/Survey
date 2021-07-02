from rest_framework import serializers
from .models import Survey, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class SurveyEditOrDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['name', 'date_finish', 'description']



