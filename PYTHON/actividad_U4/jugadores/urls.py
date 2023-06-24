from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.JugadorRetrieveAPIView.as_view()),
    path('create', views.JugadorListCreateAPIView.as_view()),
    path('delete/<int:pk>', views.JugadorDelete.as_view()),
    path('update/<int:pk>', views.JugadorUpdateAPIView.as_view()),
    path('<str:equipo>', views.api_jugador),
]