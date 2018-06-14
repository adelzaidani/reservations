from django.contrib import admin
from django.urls import path, include
from . import views

app_name='reservations'

urlpatterns = [
    path('',views.spectacles, name='liste_spectacles'),
    path('detail/<int:id_spectacle>/',views.detail, name='detail'),
    path('booking/',views.reservation, name='reservation'),
    #path('confirm_reservation/',views.confirm_reservation, name='confirm_reservation'),
]