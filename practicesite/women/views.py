from django.http import HttpResponse
from django.shortcuts import render
# Для хранения представлений (контроллеры) текущего приложения
# Create your views here.

def index(request):
    return HttpResponse('Women main page')

def categories(request):
    return HttpResponse('<h1> Articles by categories </h1>')

def texts(request):
    return HttpResponse('<i> Some text </i>')
