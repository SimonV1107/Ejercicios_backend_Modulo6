from django.shortcuts import render

from .models import Equipo
from .serializers import EquipoSerializer
from rest_framework import generics, permissions, authentication, viewsets
from django.forms.models import model_to_dict

class EquipoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class EquipoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class EquipoDelete(generics.DestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class EquipoUpdateAPIView(generics.UpdateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
  