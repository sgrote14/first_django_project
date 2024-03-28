from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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
    # response = "You're looking at the results of question %s."
    result = Choice.objects.filter(question_id=question_id).first()
    return HttpResponse(result.choice_text)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
