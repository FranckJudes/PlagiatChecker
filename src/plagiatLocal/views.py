from django.shortcuts import render

# Create your views here.


def plagiatLocal(request):
    return render(request, "locale/index.html")