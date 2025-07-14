from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    text = "Добро пожаловать в мой магазин!"
    return HttpResponse(text)