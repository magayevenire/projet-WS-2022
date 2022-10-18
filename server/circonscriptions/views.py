from django.shortcuts import render
from rest_framework import viewsets
from .models import Region ,Departement ,Commune ,Bureau
from .serializers import RegionSerializer ,DepartementSerializer ,CommuneSerializer, BureauSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
# Create your views here.
class RegionViewSet(viewsets.ModelViewSet):
    serializer_class =RegionSerializer
    queryset = Region.objects.all()

class DepartementViewSet(viewsets.ModelViewSet):
    serializer_class =DepartementSerializer
    queryset = Departement.objects.all()

class CommuneViewSet(viewsets.ModelViewSet):
    serializer_class =CommuneSerializer
    queryset = Commune.objects.all()


class BureauViewSet(viewsets.ModelViewSet):
    serializer_class =BureauSerializer
    queryset = Bureau.objects.all()

@api_view(['POST'])
def add_circonscriptions(request):
    if(request.data):
        regions = request.data.keys()
        for region in regions : 
            print(region)
            r = Region.objects.create(nom=region)
            departements = request.data[region].keys()
            for departement in departements : 
                d = Departement.objects.create(nom=departement,region=r)
                communes = request.data[region][departement]
                for commune in communes :
                    c = Commune.objects.create(nom=commune,departement=d)

                    for n in range(3):
                        b = Bureau.objects.create(commune=c,numero=n)



            
                

        # plan = Plans.objects.get(pk = request.data['plan'])
        # client = Client.objects.get(user = request.user.id)
        # paiement = Paiement.objects.create(client=client ,quantite = plan.nombre ,prixDAchat = plan.prix)
        # try:
        #     author, created = Author.objects.get_or_create(name='Leo Tolstoy')
        #     print(plan.stripe_price_id)
        #     checkout_session = stripe.checkout.Session.create(
        #         line_items=[
        #             {
        #                 # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
        #                 'price': f'{plan.stripe_price_id}',
        #                 'quantity': 1,
                        
        #             },
        #         ],
        #         mode='payment',
        #         customer = paiement.client.stripe_client_reference_id if paiement.client.stripe_client_reference_id else "",
        #         success_url=f'{YOUR_DOMAIN}/me/pay/{paiement.id}',
        #         cancel_url=f'{YOUR_DOMAIN}/me/pay/{paiement.id}',
        #     )
        #     paiement.stripe_id = checkout_session.id
        #     paiement.stripe_payment_intent = checkout_session.payment_intent
        #     paiement.save()
            

        return Response('checkout_session', status=status.HTTP_201_CREATED)


        # except Exception as e:
        #     print(str(e))
        #     return Response({"Error":"stripe error"}, status=status.HTTP_400_BAD_REQUEST)

    else :
        return Response({"Error":"Missing input"}, status=status.HTTP_400_BAD_REQUEST)
    