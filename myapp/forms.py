from django import forms
from .models import Question, Quiz

class quizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"

class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ["quiz_name",]
