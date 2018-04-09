# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import generics
from .serializers import TickSerializer
from .models import Ticks


class ListView(generics.ListAPIView):
    queryset = Ticks.objects.all()
    serializer_class = TickSerializer


class CreateView(generics.CreateAPIView):
    serializer_class = TickSerializer

    def post_data(self,serializer):
        serializer.save()

class SymbolView(generics.ListAPIView):
    serializer_class = TickSerializer

    def get_queryset(self):
        symbol = self.kwargs['symbol']
        symbol = str(symbol).upper() # All Symbols are in Upper Case
        queryset = Ticks.objects.filter(symbol=symbol)
        return queryset



# Create your views here.
