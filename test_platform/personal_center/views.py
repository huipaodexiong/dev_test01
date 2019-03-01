from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    name = request.GET.get("name", "")
    talk = []
    for i in range(3):
        talk.append("hello," + name + "\n")
    return HttpResponse(talk)