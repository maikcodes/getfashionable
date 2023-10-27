from django.http import HttpResponse
from django.views import View

class Catalog(View):
    def most_relevant(self):
        return HttpResponse('<h1>most relevant</h1>')


