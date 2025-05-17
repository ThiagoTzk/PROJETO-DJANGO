from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Core
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    
    # Quartos
    path('', views.home_view, name='home'),
    path('quartos/', views.quartos_view, name='quartos'),
    path('quartos/detalhes/<int:quarto_id>/', views.quartos_detalhes, name='quartos_detalhes'),
    
    # Gestão de Quartos (Proprietário)
    path('quartos/novo/', views.criar_quarto, name='criar_quarto'),
    path('quartos/meus/', views.meus_quartos, name='meus_quartos'),
    path('quartos/editar/<int:quarto_id>/', views.editar_quarto, name='editar_quarto'),
    path('quartos/excluir/<int:quarto_id>/', views.excluir_quarto, name='excluir_quarto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]