from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializer import ArticleSerializer
from finances.serializer import DepositSerializer, SavingSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'



class ArticleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

