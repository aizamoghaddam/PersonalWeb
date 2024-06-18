from django.shortcuts import render
from django.views import View


class DesignView(View):
    def get(self, request):
        return render(request, 'design/design.html')