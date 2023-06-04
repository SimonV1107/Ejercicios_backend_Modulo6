from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.EquipoRetrieveAPIView.as_view()),
    path('create', views.EquipoListCreateAPIView.as_view()),
    path('delete/<int:pk>', views.EquipoDelete.as_view()),
    path('update/<int:pk>', views.EquipoUpdateAPIView.as_view()),
]