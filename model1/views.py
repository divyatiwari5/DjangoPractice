from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.


def index(request):
    latest_question_request = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_request])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Detail section %s," % question_id)


def results(request, question_id):
    response = "Result section %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Voting section %s  "% question_id)

