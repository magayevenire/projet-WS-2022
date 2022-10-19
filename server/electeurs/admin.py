from django.contrib import admin
from .models import Electeur ,Candidature ,Vote,ElecteurVote
# Register your models here.
admin.site.register(Electeur)
admin.site.register(Candidature)
admin.site.register(Vote)
admin.site.register(ElecteurVote)