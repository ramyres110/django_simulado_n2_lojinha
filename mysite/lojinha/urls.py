from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.page_inicio, name="inicio"),
    path('produto/<int:produto_id>', views.page_produto_detalhe, name='produto_detalhe'),
    path('contato/', views.page_contato, name="contato"),
    path('promocao/', views.page_promocao, name="promocao"),
]