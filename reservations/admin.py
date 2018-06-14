from django.contrib import admin
from django.contrib.admin import AdminSite
from . models import ArtisteType, Artists, Shows, Localities, Locations, ArtisteTypeShow, Representations,Types,Catalog,Category


# Register your models here.


admin.site.register(Artists),
admin.site.register(Shows),
admin.site.register(Localities),
admin.site.register(Locations),
admin.site.register(Representations),
admin.site.register(Types),
admin.site.register(Catalog),
admin.site.register(Category)

