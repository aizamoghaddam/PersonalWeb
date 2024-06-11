from django.urls import path
from .views import *


app_name = 'resume'
urlpatterns = [
    path('', ResumeView.as_view(), name='resume')
]