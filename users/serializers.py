from rest_framework import serializers
from .models import Developer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _
class DevMainSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)
    
    def create(self, validated_data):
        email = validated_data.get('email') 
        password = validated_data.get('password')
        return Developer.objects.create_user(email=email,password=password)
         
            
    
class Dev2ndSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    mobile = serializers.CharField()
    profile = serializers.FileField()
    role = serializers.CharField()
    skills = serializers.CharField()
    experience = serializers.IntegerField()
                                              
    def create(self, validated_data):
        id = validated_data.get('id')
        name = validated_data.get('name')
        mobile = validated_data.get('mobile')
        profile = validated_data.get('profile')
        role = validated_data.get('role')
        skills = validated_data.get('skills').split(',')
        experience = validated_data.get('experience')
        
        dev = Developer.objects.get(id=id)

        dev.name = name
        dev.mobile = mobile
        dev.profile = profile
        dev.role = role
        dev.skills = {'skills':skills}
        dev.experience = experience
        dev.save()
        return dev
        
        
        
class Dev3rdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    p_role = serializers.CharField(allow_null=True)
    p_company = serializers.CharField(allow_null=True)
    portfolio_link = serializers.URLField(allow_null=True)
    price = serializers.IntegerField()
    education = serializers.CharField()
    work_mode = serializers.CharField()
    summary = serializers.CharField()
    
    def create(self, validated_data):
        id = validated_data.get('id')
        p_role = validated_data.get('p_role')
        p_company = validated_data.get('p_company')
        portfolio_link = validated_data.get('portfolio_link')
        price = validated_data.get('price')
        education = validated_data.get('education')
        work_mode = validated_data.get('work_mode')
        summary = validated_data.get('summary')
        
        dev = Developer.objects.get(id=id)

        dev.p_role = p_role
        dev.p_company = p_company
        dev.portfolio_link = portfolio_link
        dev.price = price
        dev.education = education
        dev.work_mode = work_mode
        dev.summary = summary
        dev.save()
        return dev


class DevLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        dev = authenticate(email=email,password=password)
        
        if dev == None:
            raise NotFound(_('Developer Not Found..!'))
        
        refresh_token = RefreshToken.for_user(dev)

        data = {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }
        return data
        
    
