from django.shortcuts import render, redirect
from plagiatLocal.forms import DocumentForm
from api.workfile import *

# Create your views here.


def plagiatLocal(request):
    return render(request, "locale/index.html")


def send_fichier(request):
    fichier = str(request.FILES['nomdoc'])
    if request.method == 'POST':
        if Typefile(fichier) == "pdf":
            doc = DocumentForm(request.POST,request.FILES)
            if doc.is_valid():
                    doc.save()
                    return redirect("plagiatLocal")                
    

def send_fichier2(request):
    fichier = str(request.FILES['nomdoc'])
    if request.method == 'POST':
        if Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
            doc = DocumentForm(request.POST,request.FILES)
            if doc.is_valid():
                    doc.save()
                    return redirect("plagiatLocal")
    