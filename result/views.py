from django.shortcuts import render
from rest_framework.generics import ListAPIView , GenericAPIView
from rest_framework.response import Response
from users.models import Developer
from random import randint
from django.db.models import F
from rest_framework import serializers

class FilterSerializer(serializers.Serializer):
    key = serializers.CharField()
    sort = serializers.CharField()
    work_mode = serializers.CharField()
    exp = serializers.CharField()
    salary = serializers.CharField()


class SearchAndFilterView(GenericAPIView):
    
    serializer_class = FilterSerializer
    queryset = Developer.objects.all()
    
    def post(self,request):        
        key = request.data.get('key',None)
        sort = request.data.get('sort',None)
        experience = request.data.get('exp',None)
        salary = request.data.get('salary',None)
        if salary is not None:
            salary = salary.split('-')
            salary_start = salary[0]
            salary_end = salary[1]
        work_mode = request.data.get('work_mode','a')
        
        # main objects
        if key == None or key == 'freshers' or key == 'experience':
            key_devs = self.queryset
        else:
            key_devs = self.queryset.filter(role__icontains = key)
        
        #filters
        filtered_devs = key_devs
        if experience == 'f':
            filtered_devs = filtered_devs.filter(experience = 0)
        elif experience == 'e':
            filtered_devs = filtered_devs.filter(experience__gt = 0)
        elif experience == 'se':
            filtered_devs = filtered_devs.filter(role__icontains = F('p_role'),experience__gt = 0) | filtered_devs.filter(p_role__icontains = F('role'),experience__gt = 0)
        elif experience == '1':
            filtered_devs = filtered_devs.filter(experience = 1)
        elif experience == '2':
            filtered_devs = filtered_devs.filter(experience = 2)
        elif experience == '3':
            filtered_devs = filtered_devs.filter(experience = 3)
        elif experience == '4':
            filtered_devs = filtered_devs.filter(experience = 4)
        elif experience == '5':
            filtered_devs = filtered_devs.filter(experience = 5)
        elif experience == '6':
            filtered_devs = filtered_devs.filter(experience = 6)
        elif experience == '7':
            filtered_devs = filtered_devs.filter(experience = 7)
        elif experience == '8':
            filtered_devs = filtered_devs.filter(experience = 8)
        elif experience == '9':
            filtered_devs = filtered_devs.filter(experience = 9)
        elif experience == '10':
            filtered_devs = filtered_devs.filter(experience = 10)    
        elif experience == '11':
            filtered_devs = filtered_devs.filter(experience__gt = 10)
            
        # return Response(filtered_devs.values())
        filtered_devs = filtered_devs.filter(price__gte = int(salary_start),price__lte = int(salary_end))
    
        if work_mode != 'a':
            filtered_devs = filtered_devs.filter(work_mode = work_mode)
            
        if sort == 'lth':
            filtered_devs = filtered_devs.order_by('price')
        elif sort == 'htl':
            filtered_devs = filtered_devs.order_by('-price')
        
        
            
        return Response(filtered_devs.values('name','role','experience','p_company','price','profile'))
        
        