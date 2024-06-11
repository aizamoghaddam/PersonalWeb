from django.shortcuts import render
from django.views import View


class SkillsView(View):
    def get(self, request):
        return render(request, 'skills/Skills.html')