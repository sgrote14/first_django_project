from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:3]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choices = Choice.objects.filter(question_id=question_id)
        context = {"question": question, "choices": choices}
        return render(request, "polls/detail.html", context)

    except Question.DoesNotExist:
        return HttpResponseNotFound("Question not found")


def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    vote_results = Choice.objects.filter(question_id=question_id)
    context = {"question": question, "vote_results": vote_results}
    return render(request, "polls/results.html", context)


def vote(request, question_id):
    print(request.POST)
    # I have the choice ID (from request object) and the question ID
    # I need to update the votes field of the choice object selected (add 1)
    selected_choice = Choice.objects.get(pk=request.POST['choice'])
    current_votes = selected_choice.votes
    selected_choice.votes = current_votes + 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
