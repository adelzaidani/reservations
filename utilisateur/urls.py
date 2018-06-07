from django.contrib import admin
from django.urls import path, include
from . import views



app_name='utilisateur'

urlpatterns = [
    path('inscription/',views.inscription, name='inscription'),
    path('inscription_test/',views.inscription_test, name='inscription_test'),
    path('connexion/',views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

]