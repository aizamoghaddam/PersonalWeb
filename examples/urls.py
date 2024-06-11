from django.urls import path
from .views import *


app_name = 'examples'
urlpatterns = [
    path('', ExampleView.as_view(), name='example')
]