from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from pathlib import Path



class AboutView(TemplateView):
    template_name = "./citylore/lore/about.html"

class HelloView(View):
    def get(self, request, *args, **kwargs):
        BASE_DIR = Path(__file__).resolve().parent.parent
        return HttpResponse("Hello world!" / BASE_DIR / 'templates/')

