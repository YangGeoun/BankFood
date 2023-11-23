from rest_framework import serializers
from .models import Youtube, News, Exchange, Index, Stock

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = '__all__'



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'

        

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

        

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'

        