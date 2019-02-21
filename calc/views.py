from django.shortcuts import render

# Create your views here.
def Calculadora (request):
  
  return render(request, 'calc/calc.html')