from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    mi_html = [f"<li>{q.question_text}</li>" for q in Question.objects.all()]
    return HttpResponse(mi_html)