from django.urls import path
from . views import *


app_name = 'design'
urlpatterns = [
    path('', DesignView.as_view(), name='design')
]