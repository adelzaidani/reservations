from django.contrib import admin
from django.urls import path, include
from . import views

app_name='reservations'

urlpatterns = [
    path('',views.spectacles, name='liste_spectacles'),
    path('detail/<int:id_spectacle>/',views.detail, name='detail'),
    path('booking/',views.reservation, name='reservation'),
    path('categorie/',views.categorie, name='categorie'),
    path('categorie/<int:id_categorie>/',views.spectacle_categu, name='spectale_parcategorie'),
    path('modif_bookable/',views.modif_bookable,name='modifier_bookable'),
    #path('confirm_reservation/',views.confirm_reservation, name='confirm_reservation'),
]