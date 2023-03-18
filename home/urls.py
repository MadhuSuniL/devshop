from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #ai views
    path('ai_sample/',AISampleDevsView.as_view()),
    path('ai_all/',AIAllDevsView.as_view()),
    
    #data science views
    path('data_science_sample/',DataScienceSampleDevsView.as_view()),
    path('data_science_all/',DataScienceAllDevsView.as_view()),

    #android views
    path('android_sample/',AndroidSampleDevsView.as_view()),
    path('android_all/',AndroidAllDevsView.as_view()),
    
    #ML views
    path('ml_sample/',MLSampleDevsView.as_view()),
    path('ml_all/',MLAllDevsView.as_view()),

    #web views
    path('web_sample/',WebSampleDevsView.as_view()),
    path('web_all/',WebAllDevsView.as_view()),

    #count
    path('count_devs/',DevsCountView.as_view())
]