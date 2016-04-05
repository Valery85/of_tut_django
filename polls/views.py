from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader

# Create your views here.

def index(request):
#    return HttpResponse("Hello, world. It's polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def home(request):
    return HttpResponse("My home page")
    
def all(request):
    return HttpResponse("Some basic information")
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    