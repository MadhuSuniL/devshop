from django.shortcuts import render
from rest_framework.views import APIView
from users.models import Developer
from rest_framework.response import Response
# Create your views here.



class AISampleDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'ai') | self.queryset.filter(role__icontains = 'AI') | self.queryset.filter(role__icontains = 'Artificial intelligence')
        try:
            devs = devs.reverse().filter(experience__gt = 0)[0:6].values('name','experience')
        except:
            devs = devs.filter(experience__gt = 0).values('name','experience')
        return Response(devs)
    
    
class AIAllDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'ai') | self.queryset.filter(role__icontains = 'AI') | self.queryset.filter(role__icontains = 'Artificial intelligence')
        devs = devs.values()
        return Response(devs)


class DataScienceSampleDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'data science') | self.queryset.filter(role__icontains = 'Data science') | self.queryset.filter(role__icontains = 'data')
        try:
            devs = devs.filter(experience__gt = 0).reverse()[0:6].values('name','experience')
        except:
           devs = devs.filter(experience__gt = 0).values('name','experience')
        return Response(devs)
    
    
class DataScienceAllDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'data science') | self.queryset.filter(role__icontains = 'Data science') | self.queryset.filter(role__icontains = 'data')
        devs = devs.values()
        return Response(devs)

class AndroidSampleDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'android') | self.queryset.filter(role__icontains = 'app') | self.queryset.filter(role__icontains = 'mobile')
        try:
            devs = devs.filter(experience__gt = 0).reverse()[0:6].values('name','experience')
        except:
            devs.values('name','experience')
        return Response(devs)
    
    
class AndroidAllDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'android') | self.queryset.filter(role__icontains = 'app') | self.queryset.filter(role__icontains = 'mobile')
        devs = devs.values()
        return Response(devs)

class MLSampleDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'Machine Learning') | self.queryset.filter(role__icontains = 'machine learning') | self.queryset.filter(role__icontains = 'ML')
        try:
            devs = devs.filter(experience__gt = 0).reverse()[0:6].values('name','experience')
        except:
            devs.values('name','experience')
        return Response(devs)
    
    
class MLAllDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'Machine Learning') | self.queryset.filter(role__icontains = 'machine learning') | self.queryset.filter(role__icontains = 'ML')
        devs = devs.values()
        return Response(devs)

class WebSampleDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'web') | self.queryset.filter(role__icontains = 'full stack') | self.queryset.filter(role__icontains = 'frontend') | self.queryset.filter(role__icontains = 'backend')
        try:
            devs = devs.filter(experience__gt = 0).reverse()[0:6].values('name','experience')
        except:
            devs.values('name','experience')
        return Response(devs)
    
    
class WebAllDevsView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        devs = self.queryset.filter(role__icontains = 'web') | self.queryset.filter(role__icontains = 'full stack') | self.queryset.filter(role__icontains = 'frontend') | self.queryset.filter(role__icontains = 'backend')
        devs = devs.values()
        return Response(devs)


class DevsCountView(APIView):
    queryset = Developer.objects.all()
    
    def get(self,request):
        ai_devs = self.queryset.filter(role__icontains = 'ai') | self.queryset.filter(role__icontains = 'AI') | self.queryset.filter(role__icontains = 'Artificial intelligence')
        ml_devs = self.queryset.filter(role__icontains = 'Machine Learning') | self.queryset.filter(role__icontains = 'machine learning') | self.queryset.filter(role__icontains = 'ML')
        data_devs = self.queryset.filter(role__icontains = 'data science') | self.queryset.filter(role__icontains = 'Data science') | self.queryset.filter(role__icontains = 'data')
        web_devs = self.queryset.filter(role__icontains = 'web') | self.queryset.filter(role__icontains = 'full stack') | self.queryset.filter(role__icontains = 'frontend') | self.queryset.filter(role__icontains = 'backend')
        data = {
            'ai':ai_devs.count(),
            'ml':ml_devs.count(),
            'data':data_devs.count(),
            'web':web_devs.count(),
        }
        return Response(data)

