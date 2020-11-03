from django.shortcuts import render
from django.http import Http404

from .models import *

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def detail(request, question_id):
    # print(question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})
