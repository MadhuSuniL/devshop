from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import DevManager
# Create your models here.



class Developer(AbstractUser,PermissionsMixin):
    username = None
    email = models.EmailField(_('Email address'),unique=True)
    name = models.CharField(max_length=14)
    mobile = models.CharField(max_length=10)
    profile = models.FileField(upload_to='profiles')
    role = models.CharField(max_length=50)
    skills = models.JSONField(blank=True, null=True)
    experience = models.IntegerField(default=0)
    p_role = models.CharField(max_length=50)
    p_company = models.CharField(max_length=50)
    portfolio_link = models.URLField()
    price = models.IntegerField(default=0)
    education = models.CharField(max_length=50)
    work_mode = models.CharField(max_length=20,default='Work From Home')
    summary = models.TextField()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = DevManager()
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Developers"

    
    