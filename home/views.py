from django.shortcuts import render, redirect
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html',)

    def post(self, request):
        data = request.POST
        comment = Comment.objects.create(comment=data['comment'])
        comment.save()
        return redirect('home:home')
    # return render(request, 'home/home.html',)
