from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import auth
from .models import Profil
from django.contrib.auth.decorators import login_required
from .forms import  InscriptionForm,UserForm, ProfilForm
from django.db import transaction

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
        form=InscriptionForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profil.language=form.cleaned_data.get('language')
            user.save()
            login(request, user)
            return redirect('reservations:liste_spectacles')
    else:
        form=InscriptionForm()

    return render(request,'utilisateur/inscription_test.html',{'form':form})

@login_required
def profil(request):
    profil=Profil.objects.get(user=request.user)

    return render(request,'utilisateur/profil.html',{'profil':profil})

@login_required
@transaction.atomic
def edit_profil(request):
    if request.method == 'POST':
        user_form=UserForm(request.POST,instance=request.user)
        profil_form=ProfilForm(request.POST,instance=request.user.profil)
        if user_form.is_valid() and profil_form.is_valid():
            user_form.save()
            profil_form.save()
            return redirect('utilisateur:profil')
    else:
        user_form=UserForm(instance=request.user)
        profil_form=ProfilForm(instance=request.user.profil)
    return render(request,'utilisateur/edit_profil.html',{'user_form':user_form,'profil_form':profil_form})
