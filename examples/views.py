from django.shortcuts import render
from django.views import View


class ExampleView(View):
    def get(self, request):
        return render(request, 'examples/Examples.html')