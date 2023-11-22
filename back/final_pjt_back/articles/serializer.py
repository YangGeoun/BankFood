from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


            
class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.nickname')
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author',)



class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.nickname')
    article_title = serializers.ReadOnlyField(source='article.title')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author','article')

