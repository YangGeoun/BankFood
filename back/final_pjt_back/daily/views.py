import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Youtube
from .serializer import YoutubeSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def youtube(request):
    youtubes = Youtube.objects.all()
    serializer = YoutubeSerializer(youtubes,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def getYoutube(request):
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&key=AIzaSyDhIuh0Zm5__5XL7Mb6MjhNdsLb_EENEOc&q=금융&maxResults=10'
    response = requests.get(url).json()
    for video in response.get('items'):
        youtube = Youtube()
        youtube.title = video.get('snippet').get('title')
        youtube.description = video.get('snippet').get('description')
        youtube.video_id = video.get('id').get('videoId')
        youtube.image_url = video.get('snippet').get('thumbnails').get('high').get('url')
        youtube.save()