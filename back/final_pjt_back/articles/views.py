from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Article, Comment
from .serializer import ArticleSerializer, CommentSerializer
from finances.serializer import DepositSerializer, SavingSerializer

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response(serializer.data , status=status.HTTP_201_CREATED)

    


    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        username = article.author
        user = get_user_model().objects.get(username='dirjsdn2365')
        data = [serializer.data]
        product_list = []
        print(user.deposit_set.all())
        for el in user.deposit_set.all():
            product_list.append(DepositSerializer(el).data)
        for el in user.saving_set.all():
            product_list.append(SavingSerializer(el).data)
            
        return Response([data,product_list])
    elif request.method == 'PUT':
        if request.user == article.author:
            serializer = ArticleSerializer(article,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response('you are not author',status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user == article.author:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('you are not author',status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comments(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user,article=article)
            return Response(serializer.data , status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request,article_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if request.user == comment.author:
            serializer = CommentSerializer(comment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response('you are not author',status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user == comment.author:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('you are not author',status=status.HTTP_403_FORBIDDEN)