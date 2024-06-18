from django.urls import path
from . views import *


app_name = 'articles'
urlpatterns = [
    path('', ArticlesView.as_view(), name='articles')
]