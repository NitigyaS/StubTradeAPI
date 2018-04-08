# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ticks(models.Model):
    """This class represents the Ticks Model."""
    class Meta:
        unique_together = (('symbol', 'date'),)

    symbol = models.CharField(max_length=15 , blank=False)
    series = models.CharField(max_length=5,blank=False)
    date = models.DateField(blank=False)
    prev_close = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    open_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    high_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    low_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    last_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    close_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    average_price = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    total_traded_quantity = models.IntegerField(blank=False)
    turnover = models.DecimalField(blank=False , decimal_places=2 , max_digits=20)
    no_trades = models.IntegerField(blank=False)
    deliverable_qty = models.IntegerField(blank=False)
    percent_del_to_trade = models.DecimalField(blank=False , decimal_places=2 , max_digits=4)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.symbol , self.open_price , self.close_price , self.low_price , self.high_price ,self.total_traded_quantity)