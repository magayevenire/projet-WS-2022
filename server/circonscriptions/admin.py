from django.contrib import admin
from .models import Region , Departement ,Commune ,Bureau

# Register your models here.
admin.site.register(Region)
admin.site.register(Departement)
admin.site.register(Commune)
admin.site.register(Bureau)