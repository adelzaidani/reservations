from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import auth
from .forms import InscriptionForm, ProfilForm

def inscription(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return  redirect('reservations:liste_spectacles')
    else:
        form=UserCreationForm()
    return render(request,'utilisateur/inscription.html',{'form':form})

def connexion(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('reservations:liste_spectacles')
    else:
        form=AuthenticationForm()
    return render(request,'utilisateur/connexion.html',{'form':form})

def deconnexion(request):
    auth.logout(request)
    return render(request,'reservations/index.html')

def inscription_test(request):
    if request.method == 'POST':
        formUser = InscriptionForm(request.POST)
        formProfil= ProfilForm(request.POST)
        if formUser.is_valid() and formProfil.is_valid():
            user=formUser.save()
            profil=formProfil.save()
    else:
        formUser=InscriptionForm()
        formProfil=ProfilForm()

    return render(request,'utilisateur/inscription_test.html',{'formUser':formUser,'formProfil':formProfil})

