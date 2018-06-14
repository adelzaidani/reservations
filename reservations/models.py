from django.db import models
from utilisateur.models import Profil
from datetime import datetime
from django.contrib.auth.models import User


class ArtisteType(models.Model):
    artist = models.ForeignKey('Artists', models.DO_NOTHING)
    type = models.ForeignKey('Types', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'artiste_type'




class ArtisteTypeShow(models.Model):
    show = models.ForeignKey('Shows', models.DO_NOTHING)
    artiste_type = models.ForeignKey(ArtisteType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'artiste_type_show'
        verbose_name_plural = 'Artiste Type de Spéctacles'


class Artists(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'artists'
        verbose_name_plural= 'Artistes'
        verbose_name = 'Artiste'
    def __str__(self):
        return self.lastname +' - '+self.firstname


class Localities(models.Model):
    postal_code = models.CharField(unique=True, max_length=6)
    locality = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'localities'
        verbose_name_plural = 'Localités'
        verbose_name = 'Localité'
    def __str__(self):
        return self.postal_code +' - '+ self.locality


class Locations(models.Model):
    slug = models.CharField(unique=True, max_length=60)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    locality = models.ForeignKey(Localities, models.DO_NOTHING)
    website = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    available_places=models.IntegerField(default=0, verbose_name='Places disponibles')
    number_of_places_sold=models.IntegerField(default=0, verbose_name='Places vendues')

    class Meta:
        managed = False
        db_table = 'locations'
        verbose_name_plural= 'Emplacements'
        verbose_name = 'Emplacement'

    def __str__(self):
        return self.designation

    def get_available_places(self):
        return self.available_places

    def get_number_of_places_sold(self):
        return self.number_of_places_sold


class Representations(models.Model):
    show = models.ForeignKey('Shows', models.DO_NOTHING)
    when = models.DateTimeField()
    location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.show.__str__() + '-'+ self.when.__str__() + '-'+ self.location.__str__()

    class Meta:
        managed = False
        db_table = 'representations'
        verbose_name_plural = 'Representations'
        verbose_name = 'Representation'


class Category(models.Model):
    titre = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.titre


class Shows(models.Model):
    slug = models.CharField(unique=True, max_length=60)
    title = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    bookable = models.BooleanField()
    price=models.FloatField(default=20)
    category = models.OneToOneField(Category,on_delete=models.CASCADE,default=4)


    class Meta:
        managed = False
        db_table = 'shows'
        verbose_name_plural = 'Spéctacles'
        verbose_name = 'Spéctacle'

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price

    def reservable(self):
        return self.bookable



class Catalog(models.Model):
    year=models.CharField(unique=True,max_length=30,default='2017/2018')
    shows=models.ForeignKey(Shows,on_delete=models.CASCADE,default=1)

    class Meta:
        verbose_name_plural = 'Catalogues'
        verbose_name = 'Catalogue'
    def __str__(self):
        return self.year

class Types(models.Model):
    type = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'types'
        verbose_name_plural = 'Types'
        verbose_name = 'Type'
    def __str__(self):
        return self.type


class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=12)
    date_reservation=models.DateTimeField(auto_now_add=True)
    nombre_place=models.IntegerField()
    prix_total=models.FloatField()
    spectacle=models.ForeignKey(Shows,on_delete=models.CASCADE)
    location=models.ForeignKey(Locations,on_delete=models.CASCADE)



