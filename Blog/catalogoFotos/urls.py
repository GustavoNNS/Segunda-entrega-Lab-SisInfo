from django.urls import path

from . import views

app_name = 'catalogo'
urlpatterns = [
    path('<int:foto_id>/', views.detail_foto_detailView.as_view(), name='detail'),
    path('', views.catalogo_fotos_listView.as_view(),name='index'),
    path('busca/', views.busca_fotos, name='busca'),
    path('postar_foto/', views.postar_foto_createView.as_view(), name='postar'),
    path('atualizar_post/<int:foto_id>/', views.atualizar_post_updateView.as_view(), name='atualizar'),
    path('deletar/<int:foto_id>/', views.deletar_foto_deleteView.as_view(), name='deletar')

]