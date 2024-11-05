from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Collec

# Create your views here.
def about(request):
    return HttpResponse("Description de l'application")


def collection_detail(request, n):
    collection = get_object_or_404(Collec, id=n)
    return render(request, 'collec_management/collection_detail.html', {'collection': collection})