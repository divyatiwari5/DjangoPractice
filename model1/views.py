from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.http import Http404
from django.views import generic
from django.utils import timezone

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:3]
#     template = loader.get_template('model1/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#
#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'model1/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'model1/result.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'model1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return last 5 published questions(not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'model1/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet"""

        return Question.objects.filter(pub_date__lte=timezone.now())




class ResultsView(generic.DetailView):
    model = Question
    template_name =  'model1/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'model1/detail.html', {
            'question': question,
            'error_message': "Please choose from the below options!"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('model1:results', args=(question.id,)))

