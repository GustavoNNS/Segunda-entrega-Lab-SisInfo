from django.urls import path

from . import views

app_name = 'catalogo'
urlpatterns = [
    path('<int:foto_id>/', views.detail_foto, name='detail'),
    path('', views.catalogo_fotos,name='index')
]