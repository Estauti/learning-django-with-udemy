from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.person_list, name='person_list'),
    path('pessoas/cadastrar/', views.person_new, name='person_new'),
    path('pessoas/<int:id>/', views.person_edit, name='person_edit'),
    path('pessoas/deletar/<int:id>/', views.person_delete, name='person_delete'),
]