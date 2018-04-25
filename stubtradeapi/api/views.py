# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import generics
from .serializers import TickSerializer
from .models import Ticks

import re



class ListView(generics.ListAPIView):
    """
    Returns all the data of all Stocks
    """
    queryset = Ticks.objects.all()
    serializer_class = TickSerializer


class CreateView(generics.CreateAPIView):
    """
    post:
    Create a new stock Tick
    """
    serializer_class = TickSerializer

    def post_data(self,serializer):
        serializer.save()


class SymbolView(generics.ListAPIView):
    """
    Returns Symbol data based on time period.
    """
    serializer_class = TickSerializer

    def get_queryset(self):
        symbol = self.kwargs['symbol']
        range =  self.kwargs['range']

        days = self.get_days(range)
        symbol = str(symbol).upper() # All Symbols are in Upper Case
        queryset = Ticks.objects.filter(symbol=symbol).order_by('date')[:days]
        return queryset

    def get_days(self,range):
        pattern = re.compile('(\d+)(\w+)')
        count = pattern.match(range).group(1)
        interval = pattern.match(range).group(2)

        if interval == 'day' or interval == 'days' :
            return int(count)
        elif interval == 'month' or interval == 'months' :
            return int(int(count))*30
        elif interval == 'year' or interval == 'year' :
            return int(int(count))*365
        else:
            return 30


class ExactSymbolView(generics.ListAPIView):
    """
    :param
    Return Symbol data of one particular day
    """
    serializer_class = TickSerializer

    def get_queryset(self):
        """
        :Keyword Arguments:
        * *symbol* (``string``) --
          NSE Symbol
        * *range* (``string``) --
          (\d+)[month|day|year]

        :return:
        """
        symbol = self.kwargs['symbol']
        range = self.kwargs['range']
        days = self.get_days(range)
        symbol = str(symbol).upper()  # All Symbols are in Upper Case
        queryset = Ticks.objects.filter(symbol=symbol).order_by('date')[days-1:days]
        return queryset

    def get_days(self, range):
        pattern = re.compile('(\d+)day')
        count = pattern.match(range).group(1)
        return int(count)


# Create your views here.
