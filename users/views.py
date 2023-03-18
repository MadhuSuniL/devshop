from django.shortcuts import render
from .names import *
from .models import Developer
from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import Developer
# Create your views here.

# resgister views

class DevRegMainView(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DevMainSerializer

class DevReg2ndView(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = Dev2ndSerializer

class DevReg3rdView(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = Dev3rdSerializer
        
        
# login views 

class DevLoginView(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DevLoginSerializer



import random
        
def test(request): 

    for dev in Developer.objects.all():
        if dev.name == 'Poco X3 Pro':
            dev.delete()  
    