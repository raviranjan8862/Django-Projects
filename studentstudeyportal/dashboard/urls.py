from django.urls import path
from .import views

urlpatterns=[
    path('',views.home ,name="home"),
    path('notes/',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete-note"),
    path('notes_Detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),
    
]