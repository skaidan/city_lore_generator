from django.http import HttpResponse
from django.views import View


class AsyncView(View):
    def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        return HttpResponse("Hello async world!")