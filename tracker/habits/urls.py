from django.urls import path
from . import views

urlpatterns = [
    path('asleep/', views.asleep),
    path('awake/', views.awake),
    path('dip/', views.dip),
    path('add/', views.add),
    path('dream-notes/', views.dreamNotes)
]