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
]