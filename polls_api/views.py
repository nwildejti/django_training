from rest_framework import viewsets, permissions
from . import serializers
from polls.models import Question, Choice
# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)