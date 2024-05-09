# forms.py
from django import forms
from django.forms import inlineformset_factory

from .models import Question, Choice, Comment


# forms.py
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {
            'question_text': 'Table Name',
        }

    def save(self, user=None, commit=True):
        question = super().save(commit=False)
        if user:
            question.user = user
        if commit:
            question.save()
        return question


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    extra=3,
    can_delete=True
)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
