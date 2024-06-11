from django.shortcuts import render
from django.views import View


class ResumeView(View):
    def get(self, request):
        return render(request, 'resume/Resume.html')
