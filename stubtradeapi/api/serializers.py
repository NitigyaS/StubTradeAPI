from rest_framework import serializers
from .models import Ticks
class TickSerializer(serializers.ModelSerializer):
    """Serializer to Mapt the model into Json format.."""
    class Meta:
        """Meta class to map serializer field to Model field"""
        model = Ticks
        fields = ('id','symbol' , 'series','date','prev_close' , 'open_price' , 'high_price' , 'low_price' , 'last_price' ,
                'close_price' , 'average_price' , 'total_traded_quantity' , 'turnover' , 'no_trades' , 'deliverable_qty' ,
                'percent_del_to_trade' )