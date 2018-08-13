from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoas/', views.person_list, name='person_list'),
    path('pessoas/cadastrar/', views.person_new, name='person_new'),
    path('pessoas/<int:id>/', views.person_edit, name='person_edit'),
    path('pessoas/deletar/<int:id>/', views.person_delete, name='person_delete'),
    path('documentos/', views.document_list, name="document_list"),
    path('documentos/cadastrar/', views.document_new, name='document_new'),
    path('documentos/<int:id>/', views.document_edit, name='document_edit'),
    path('documentos/deletar/<int:id>/', views.document_delete, name='document_delete'),
    path('casas/', views.house_list, name='house_list'),
    path('casas/cadastrar/', views.house_new, name='house_new'),
    path('casas/edit/<int:id>/', views.house_edit, name='house_edit'),
    path('casas/deletar/<int:id>/', views.house_delete, name='house_delete'),
]