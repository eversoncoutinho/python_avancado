from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #toda lógica da view    
    return HttpResponse("Olá mundo")