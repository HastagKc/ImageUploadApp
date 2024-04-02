from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

# Create your views here.


def home(request):
    # return HttpResponse("Hello World")
    card = Card.objects.all()
    content = {"cards": card}
    return render(request, "index.html", context=content)
