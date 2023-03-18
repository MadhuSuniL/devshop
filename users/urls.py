from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView , TokenVerifyView , TokenObtainPairView
from .views import *

urlpatterns = [
    #token views
    path('s',test),
    path('get_token',TokenObtainPairView.as_view()),
    path('verify_token',TokenObtainPairView.as_view()),
    path('refresh_tokem',TokenObtainPairView.as_view()),

    #auth views
    path('register_main',DevRegMainView.as_view()),
    path('register_2nd',DevReg2ndView.as_view()),
    path('register_3rd',DevReg3rdView.as_view()),
    path('login',DevLoginView.as_view()),
    

]