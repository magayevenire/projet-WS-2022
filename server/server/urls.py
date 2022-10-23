"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from circonscriptions.views import RegionViewSet, DepartementViewSet , CommuneViewSet, BureauViewSet ,add_circonscriptions
from electeurs.views import ElecteurViewSet , CandidatureViewSet ,VoteViewSet ,UserViewSet
from elections.views import ElectionViewSet


router = DefaultRouter()
router.register('region',RegionViewSet,basename='region')
router.register('departement',DepartementViewSet,basename='departement')
router.register('commune',CommuneViewSet,basename='commune')
router.register('bureau',BureauViewSet,basename='bureau')
router.register('electeur',ElecteurViewSet,basename='electeur')
router.register('canditature',CandidatureViewSet,basename='canditature')
router.register('vote',VoteViewSet,basename='vote')
# router.register('electeur-vote',ElecteurVoteViewSet,basename='electeur-vote')
router.register('election',ElectionViewSet,basename='election')
router.register('user',UserViewSet,basename='user')


urlpatterns = [
    path("api/",include(router.urls)),  
    path("add_circonscriptions",add_circonscriptions),  
    path('admin/', admin.site.urls),
    # path('', admin.site.urls),
    path('', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]


