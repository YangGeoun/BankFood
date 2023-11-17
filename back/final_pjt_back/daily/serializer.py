from rest_framework import serializers
from .models import Youtube, News

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = '__all__'



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'