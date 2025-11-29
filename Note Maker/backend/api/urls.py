from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.NotesListCreateView.as_view(), name='notes-list-create'),
    path('notes/<int:pk>/', views.NotesDeleteView.as_view(), name='notes-delete'),
]