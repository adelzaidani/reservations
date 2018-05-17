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


class Artists(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'artists'


class Localities(models.Model):
    postal_code = models.CharField(unique=True, max_length=6)
    locality = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'localities'


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


class Representations(models.Model):
    show = models.ForeignKey('Shows', models.DO_NOTHING)
    when = models.DateTimeField()
    location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'representations'


class Shows(models.Model):
    slug = models.CharField(unique=True, max_length=60)
    title = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, models.DO_NOTHING)
    bookable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shows'


class Types(models.Model):
    type = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'types'


# Create your models here.
