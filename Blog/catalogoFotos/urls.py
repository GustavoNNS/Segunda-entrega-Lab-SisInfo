from django.urls import path

from . import views

app_name = 'catalogo'
urlpatterns = [
    path('<int:foto_id>/', views.detail_foto, name='detail'),
    path('', views.catalogo_fotos,name='index'),
    path('busca/', views.busca_fotos, name='busca'),
    path('postar_foto/', views.postar_foto, name='postar'),
    path('atualizar_post/<int:foto_id>/', views.atualizar_post, name='atualizar'),
    path('deletar/<int:foto_id>/', views.deletar_foto, name='deletar')

]