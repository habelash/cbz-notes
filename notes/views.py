from django.shortcuts import render
from .models import chemisrty, zoology, botany


def index(request):
    context = {
        "chem": chemisrty.objects.all(),
        "zoo": zoology.objects.all(),
        "bot": botany.objects.all()
    }

    return render(request, "index.html", context)
# Create your views here.
