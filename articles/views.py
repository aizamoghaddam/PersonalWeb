from django.shortcuts import render
from django.views import View


class ArticlesView(View):
    def get(self, request):
        return render(request, 'articles/articles.html')
