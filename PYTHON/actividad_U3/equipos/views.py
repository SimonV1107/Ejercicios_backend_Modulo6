from django.shortcuts import render

from .models import Equipo
from .serializers import EquipoSerializer
from rest_framework import generics
from django.forms.models import model_to_dict


class EquipoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class EquipoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class EquipoDelete(generics.DestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class EquipoUpdateAPIView(generics.UpdateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

