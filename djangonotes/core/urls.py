from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('create-note', views.create_note, name='create_note'),
    path('update-note/<str:noteId>', views.update_note, name='update_note'),
    path('delete-note/<str:noteId>', views.delete_note, name='delete_note'),
]
