# forms.py
from django import forms
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    choice1 = forms.CharField(label='Choice 1', max_length=200)
    choice2 = forms.CharField(label='Choice 2', max_length=200)

    class Meta:
        model = Question
        fields = ['question_text']

    def save(self, commit=True):
        question = super().save(commit=False)
        question.save()
        choice1_text = self.cleaned_data.get('choice1')
        choice2_text = self.cleaned_data.get('choice2')
        Choice.objects.create(question=question, choice_text=choice1_text)
        Choice.objects.create(question=question, choice_text=choice2_text)
        return question


class QuestionFormUPDATE(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']