from django.utils import timezone

from django.shortcuts import render



def index(request):

    data = {
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/index.html", context=data)
def index1(request):

    data = {
        'audjourdhui' : timezone.now(),
    }
    return render(request, "boutique/index1.html", context=data)
