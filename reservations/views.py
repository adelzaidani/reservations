from django.shortcuts import render
from django.http import Http404
from .models import Shows
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    return render( request,'reservations/index.html')

def detail(request,id_spectacle):
    try:
        spectacle = Shows.objects.get(pk=id_spectacle)
    except Shows.DoesNotExist:
        raise Http404("Ce spectacle n existe pas !")
    return render(request,'reservations/detail.html', {'spectacle': spectacle})


def spectacles(request):
    liste_spectacle=Shows.objects.all()
    return render(request,'reservations/spectacles.html',{'spectacles':liste_spectacle})

