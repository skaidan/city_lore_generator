from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class AboutView(TemplateView):
    template_name = "about.html"

class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world!" / BASE_DIR / 'templates/')

