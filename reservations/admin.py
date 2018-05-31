from django.contrib import admin
from . models import ArtisteType, Artists, Shows, Localities, Locations, ArtisteTypeShow, Representations,Types


# Register your models here.

admin.site.register(Artists),
admin.site.register(Shows),
admin.site.register(Localities),
admin.site.register(Locations),
admin.site.register(Representations),
admin.site.register(Types)
