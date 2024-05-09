from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice, Comment
from .forms import QuestionForm, ChoiceFormSet, CommentForm


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


@login_required(login_url='auth:login')
def create_question(request):  # Create table
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Pass the user argument to the save method
            question = form.save(commit=False, user=request.user)
            question.save()  # Now commit the question to the database
            return redirect('polls:index')  # Redirect to the homepage or wherever you want
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})


@login_required(login_url="auth:login")
def delete_question(request, question_id):  # delete table
    question = get_object_or_404(Question, pk=question_id)

    # Check if the current user is the creator of the question
    if request.user != question.user:
        return redirect('polls:index')  # Redirect to the index page or another appropriate page

    if request.method == 'POST':
        question.delete()
        return redirect('polls:index')  # Redirect to a success URL, such as the homepage

    return render(request, 'polls/delete_question_confirm.html', {'question': question})


@login_required(login_url="auth:login")
def update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Check if the current user is the creator of the question
    if request.user != question.user:
        return redirect('polls:index')

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = ChoiceFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            form.save()
            # Update choices
            choices = formset.save(commit=False)
            for choice in choices:
                choice.question = question
                choice.save()
            return redirect('polls:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
        formset = ChoiceFormSet(instance=question)
    return render(request, 'polls/update_question.html', {'form': form, 'formset': formset, 'question': question})


@login_required
def delete_choice(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user.id != question.user_id:
        return redirect('polls:detail', question_id=question.id)
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.delete()
    return redirect('polls:update', question_id=question.id)


def add_comment_to_news(request, pk):
    news = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.author = request.user  # Припускаємо, що користувач увійшов в систему
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()
    return render(request, 'your_app/comment_form.html', {'form': form})
