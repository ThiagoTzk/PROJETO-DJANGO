from django.urls import path
from home.views import home_view, quartos_detalhes
from promotions.views import index

urlpatterns = [
    path('', home_view, name='home'),
    path('quartos/', index, name='quartos'),
    path('quartos/detalhes/', quartos_detalhes, name='quartos_detalhes'),
]
