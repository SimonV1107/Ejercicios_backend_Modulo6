from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('equipos_viewset', views.EquipoViewSet, basename="equipos_viewset")

urlpatterns = [
    path('<int:pk>', views.EquipoRetrieveAPIView.as_view()),
    path('create', views.EquipoListCreateAPIView.as_view()),
    path('delete/<int:pk>', views.EquipoDelete.as_view()),
    path('update/<int:pk>', views.EquipoUpdateAPIView.as_view()),
] + router.urls

