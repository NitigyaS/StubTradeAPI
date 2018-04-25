# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ticks(models.Model):
    """This class represents the Ticks Model."""
    class Meta:
        unique_together = (('symbol', 'date'),)

    symbol = models.CharField(max_length=15 , blank=False , help_text=("Unique NSE identifier" ))
    series = models.CharField(max_length=5,blank=False , help_text=("Series" ))
    date = models.DateField(blank=False , help_text=("Date of Tick" ))
    prev_close = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("Previous Close Price" ))
    open_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("Open Price" ))
    high_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("High Price" ))
    low_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("Low Price" ))
    last_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("Last Update Price" ))
    close_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("Close Price" ))
    average_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20 , help_text=("Average Price" ))
    total_traded_quantity = models.IntegerField(blank=False , help_text=("Traded Quantity" ))
    turnover = models.DecimalField(blank=False , decimal_places=2 , max_digits=20, help_text=("Turnover" ))
    no_trades = models.IntegerField(blank=False, help_text=("Number of Trade Occured" ))
    deliverable_qty = models.IntegerField(blank=False, help_text=("Deliverd Quantity" ))
    percent_del_to_trade = models.DecimalField(blank=False , decimal_places=2 , max_digits=4, help_text=("Deliverd to Trade Percentage" ))

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.symbol , self.open_price , self.close_price , self.low_price , self.high_price ,self.total_traded_quantity)