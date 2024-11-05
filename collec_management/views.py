from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("Description de l'application")


def index(request):
    collection = Collec.objects.order_by("-titre")
    context = {}