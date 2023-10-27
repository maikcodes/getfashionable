from django.urls import path

from .views import Catalog, Home


app_name = 'getfashionable'
urlpatterns = [
    path('', Catalog.most_relevant, name='most_relevant'),
    path('home/', Home.most_recent, name='home'),
]