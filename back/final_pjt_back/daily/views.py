import html 
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Youtube, News, Exchange
from .serializer import YoutubeSerializer, NewsSerializer, ExchangeSerializer

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
        youtube.title = html.unescape(video.get('snippet').get('title'))
        youtube.description = html.unescape(video.get('snippet').get('description'))
        youtube.video_id = html.unescape(video.get('id').get('videoId'))
        youtube.image_url = html.unescape(video.get('snippet').get('thumbnails').get('high').get('url'))
        youtube.save()


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def getnews(request):
    url = 'https://openapi.naver.com/v1/search/news.json?query=금융&start=1&display=30'
    headers = {'X-Naver-Client-Id':'hA5tn6adwDPQB3ldzXJy','X-Naver-Client-Secret':'xPZUuPw7xe'}
    response = requests.get(url,headers=headers).json()
    # print(response)
    for item in response.get('items'):
        print(item.get('link'))
        if 'news.naver' in item.get('link'):
            news = News()
            news.title = html.unescape(item.get('title'))
            news.description = html.unescape(item.get('description'))
            news.naver_url = item.get('link')
            res = requests.get(item.get('link'))
            abc = res.text
            soup = BeautifulSoup(abc, 'html.parser')
            if not soup.select_one('#img1'):
                continue
            news.image_url = soup.select_one('#img1').get('data-src')
            news.save()
    return Response({'asd':'asd'})


def getexchange(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=9TbzRbWuNPvOkkXHBLwKrUDQjvK5wPWY&data=AP01'
    response = requests.get(url).json()
    exchanges = Exchange.objects.all()
    exchanges.delete()
    for excha in response:
        exchange = Exchange()
        exchange.cur_unit = excha.get('cur_unit')
        exchange.ttb = excha.get('ttb')
        exchange.tts = excha.get('tts')
        exchange.deal_bas_r = excha.get('deal_bas_r')
        exchange.bkpr = excha.get('bkpr')
        exchange.yy_efee_r = excha.get('yy_efee_r')
        exchange.ten_dd_efee_r = excha.get('ten_dd_efee_r')
        exchange.kftc_bkpr = excha.get('kftc_bkpr')
        exchange.cur_nm = excha.get('cur_nm')
        exchange.kftc_deal_bas_r = excha.get('kftc_deal_bas_r')
        exchange.save()