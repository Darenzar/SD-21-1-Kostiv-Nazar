from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F
from .forms import QuestionForm, QuestionFormUPDATE


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # If you have a field for the user who asked the question, you can set it here
            # For example: question.asked_by = request.user
            question.save()
            return redirect('polls:index')  # Redirect to the homepage or wherever you want
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})


def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        # If the request method is POST, delete the question
        question.delete()
        # Redirect to a success URL, such as the homepage
        return redirect('polls:index')  # Replace 'home' with the name of your homepage URL pattern

        # Render a confirmation template if the request method is GET
    return render(request, 'polls/delete_question_confirm.html', {'question': question})


def update(request, question_id):
    # Retrieve the question object or return a 404 error if not found
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = QuestionFormUPDATE(request.POST, instance=question)
        if form.is_valid():
            form.save()  # Save the updated question
            return redirect('polls:detail', question_id=question_id)  # Redirect to the question's detail page
    else:
        # If the request method is GET, render the form with the current question data
        form = QuestionFormUPDATE(instance=question)

    # Render the form template with the form data
    return render(request, 'polls/update_question.html', {'form': form, 'question': question})