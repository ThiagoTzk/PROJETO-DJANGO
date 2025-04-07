from django.urls import path
from home.views import home_view, quartos_view, quartos_detalhes

urlpatterns = [
    path('', home_view, name='home'),
    path('quartos/', quartos_view, name='quartos'),
    path('quartos/detalhes/', quartos_detalhes, name='quartos_detalhes'),
]