# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [

#     path('', views.signin),
#     path('signin', views.signin),
#     path('signup', views.signup),
#     path('forgot', views.password_reset_form),
#     path('deconnexion', views.deconnexion),

# ]

from django.urls import path
from myauth.views import MyObtainTokenPairView, RegisterView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenRefreshView 
from .views import LoginView
    

urlpatterns = [
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # path('login/', views.obtain_auth_token, name='api-token-auth'),
    # path('login/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name="login"),
    
]
