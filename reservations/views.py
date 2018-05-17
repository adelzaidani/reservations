from django.shortcuts import render
from .models import Shows

# Create your views here.


def index(request):
    return render( request,'reservations/index.html')

def spectacles(request):
    liste_spectacle=Shows.objects.all()
    return render(request,'reservations/spectacles.html',{'spectacles':liste_spectacle})