from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def formulario(request):

  return HttpResponse('<h1> Olá Mundo! </h1> ')