from django.shortcuts import render

from .models import Jugador
from .serializers import JugadorSerializer
from rest_framework import generics
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

class JugadorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class JugadorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class JugadorDelete(generics.DestroyAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class JugadorUpdateAPIView(generics.UpdateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

@api_view(['GET'])
def api_jugador(request, equipo, *arg, **kwargs):
    data = {}
    instances = Jugador.objects.filter(equipo__contains=equipo)
    if instances:
            data = JugadorSerializer(instances, many=True).data

    return Response(data)
