from django.urls import path
from . import views

urlpatterns = [
    path('sleep/', views.sleep),
    path('wake/', views.wake),
    path('dip/', views.dip)
]