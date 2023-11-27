from django.shortcuts import render
from api.workfile import *

# Create your views here.


def plagiatLocal(request):
    return render(request, "locale/index.html")


def send_fichier(request):
    fichier = str(request.FILES['fichier'])
    
    if Typefile(fichier) == "pdf":
        EnregistrerPDF(request.FILES['fichier'])
        
    elif Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
        Enregistrerautre(request.FILES['fichier']) 
        
    return render(request, "locale/index.html")

def send_fichier2(request):
    fichier = str(request.FILES['fichier'])
        
    if Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
        Enregistrerautre(request.FILES['fichier']) 
        
    return render(request, "locale/index.html")