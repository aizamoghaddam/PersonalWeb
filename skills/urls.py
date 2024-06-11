from django.urls import path
from .views import *


app_name = 'skills'
urlpatterns = [
    path('', SkillsView.as_view(), name='skills')
]