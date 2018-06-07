from django.db import models


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

    class Meta:
        managed = False
        db_table = 'locations'
        verbose_name_plural= 'Emplacements'
        verbose_name = 'Emplacement'

    def __str__(self):
        return self.designation


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


class Shows(models.Model):
    slug = models.CharField(unique=True, max_length=60)
    title = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    bookable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shows'
        verbose_name_plural = 'Spéctacles'
        verbose_name = 'Spéctacle'
    def __str__(self):
        return self.title


class Types(models.Model):
    type = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'types'
        verbose_name_plural = 'Types'
        verbose_name = 'Type'
    def __str__(self):
        return self.type

# Create your models here.
