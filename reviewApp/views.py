from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cocktails


# Create your views here.
def index(request):
    return HttpResponse("Test URL")


def home(request, lastPage):
    context = {
        "lastPage": lastPage
    }
    return render(request, "reviewApp/home.html", context)

def page2(request, lastPage):
    context = {
        "lastPage": lastPage
    }
    return render(request, "reviewApp/page2.html", context)

def page3(request, lastPage):
    context = {
        "lastPage": lastPage
    }
    return render(request, "reviewApp/page3.html", context)

def page4(request, lastPage):
    context = {
        "lastPage": lastPage
    }
    return render(request, "reviewApp/page4.html", context)

def page5(request, lastPage):
    context = {
        "lastPage": lastPage
    }
    return render(request, "reviewApp/page5.html", context)


def cocktails(request):

    allCocktails = Cocktails.objects.all()

    context = {
        "allCocktails": allCocktails
    }

    return render(request, "reviewApp/cocktails.html", context)


def details(request, drink):

    selectedDrink = get_object_or_404(Cocktails, pk=drink)

    context = {
        "drink": selectedDrink,
    }

    return render(request, "reviewApp/details.html", context)