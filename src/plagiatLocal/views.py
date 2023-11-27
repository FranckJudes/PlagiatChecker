from django.shortcuts import render
from api.workfile import *

# Create your views here.


def plagiatLocal(request):
    return render(request, "locale/index.html")


def send_fichier(request):
    EnregistrerPDF(request.FILES['fichier'])
    return render(request, "locale/index.html")