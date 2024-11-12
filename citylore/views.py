from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world!")

