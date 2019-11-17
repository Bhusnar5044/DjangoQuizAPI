from rest_framework import serializers
from .models import Quiz, Questions

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model=Quiz
        fields='__all__'
        # fields=('sum',)

class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Questions
        fields='__all__'
        # fields=('sum',)