

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from rest_framework import status
from .forms import SignupForm
from api.models import Client

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@permission_classes([AllowAny])

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()        
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = data["access"],
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {"Success" : "Login successfully","data":data}
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([AllowAny])
class SignView(APIView): 


    def post(self, request, format=None):
        response = Response() 
        formCompte = SignupForm(request.POST or None)

        envoi = False
        if formCompte.is_valid() : 
            print("valid")
            user = formCompte.save()
            client = Client.objects.create(user=user)
            # formCompte.send_email()

            envoi = True  
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                
            if user is not None:
                if user.is_active:
                    data = get_tokens_for_user(user)
                    # response.set_cookie(
                    #     key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    #     value = data["access"],
                    #     expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    #     secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    #     httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    #     samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                    # )
                    # csrf.get_token(request)
                    response.data = {"Success" : "Login successfully","data":data}
                    return response
                else:
                    return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            print(formCompte.errors)
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
