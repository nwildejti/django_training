from rest_framework import serializers

from polls.models import Question, Choice
class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(view_name='question-detail', read_only=True)
    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')

class QuestionChoiceSerializer(serializers.ModelSerializer):
    choice = serializers.HyperlinkedIdentityField(view_name='choice-detail')

    class Meta:
        model = Choice
        fields = ('choice', 'choice_text', 'votes')

class QuestionSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'choices')


