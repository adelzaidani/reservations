from django.shortcuts import render
from django.http import Http404
from .models import Shows,Reservation,Category
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    return render( request,'reservations/index.html')



def detail(request,id_spectacle):
    try:
        spectacle = Shows.objects.get(pk=id_spectacle)
    except Shows.DoesNotExist:
        raise Http404("Ce spectacle n existe pas !")
    if request.method=='POST':
        nombre_place=int(request.POST.get("nombre_place"))
        place_dispo= spectacle.location.get_available_places()
        if (place_dispo >= nombre_place):
            total= nombre_place*spectacle.get_price()
            current_user=request.user
            location=spectacle.location
            booking=Reservation.objects.create(
                user=current_user,
                nombre_place=nombre_place,
                prix_total=total,
                spectacle=spectacle,
                location=location
            )



    return render(request,'reservations/detail.html', {'spectacle': spectacle})


def spectacles(request):
    spectacle_dispo = Shows.objects.filter(bookable=True)
    return render(request,'reservations/spectacles.html',{'spectacle_dispo':spectacle_dispo})



@login_required(login_url='/utilisateur/connexion/')
def reservation(request):
    spectacle_dispo=Shows.objects.filter(bookable=True)
    return render(request,'reservations/reservations.html',{'spectacle_dispo':spectacle_dispo})

def categorie(request):
    categories=Category.objects.all()
    return render(request,'reservations/categories.html',{'categories':categories})

def spectacle_categu(request,id_categorie):
    spectacles=Shows.objects.filter(category=id_categorie)
    return render(request, 'reservations/spectacle_category.html', {'spectacles': spectacles})

def modif_bookable(request,data):

    pass