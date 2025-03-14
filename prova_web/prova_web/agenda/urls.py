from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contatos/', views.lista_contatos, name='lista_contatos'),
    path('contatos/<int:id>/', views.agenda_detalhe, name='agenda_detalhe'),

]