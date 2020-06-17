from django.shortcuts import render
from .models import chemisrty, zoology, botany, sem1, sem2, sem3, sem4, sem5, sem6


def index(request):
    return render(request, "index.html")


# Create your views here.


def chem(request):
    context = {
        "subs": chemisrty.objects.all(),
        "subject": 'Chemistry',
    }
    return render(request, 'notes.html', context)


def zoo(request):
    context = {
        "subs": zoology.objects.all(),
        "subject": 'Zoology',
    }
    return render(request, 'notes.html', context)


def bot(request):
    context = {
        "subs": botany.objects.all(),
        "subject": 'Botany'

    }
    return render(request, 'notes.html', context)


def semister1(request):
    context = {
        "subs": sem1.objects.all(),
        "subject": 'Semister-1'

    }
    return render(request, 'notes.html', context)


def semister2(request):
    context = {
        "subs": sem2.objects.all(),
        "subject": 'Semister-2'

    }
    return render(request, 'notes.html', context)



def semister3(request):
    context = {
        "subs": sem3.objects.all(),
        "subject": 'Semister-3'

    }
    return render(request, 'notes.html', context)


def semister4(request):
    context = {
        "subs": sem4.objects.all(),
        "subject": 'Semister-4'

    }
    return render(request, 'notes.html', context)


def semister5(request):
    context = {
        "subs": sem5.objects.all(),
        "subject": 'Semister-5'

    }
    return render(request, 'notes.html', context)


def semister6(request):
    context = {
        "subs": sem6.objects.all(),
        "subject": 'Semister-6'

    }
    return render(request, 'notes.html', context)
