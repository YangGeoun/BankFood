import html 
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Youtube, News, Exchange, Stock, Index
from .serializer import YoutubeSerializer, NewsSerializer, ExchangeSerializer, IndexSerializer, StockSerializer

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
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&key=AIzaSyDhIuh0Zm5__5XL7Mb6MjhNdsLb_EENEOc&q=금융&maxResults=10'
    response = requests.get(url).json()
    for video in response.get('items'):
        youtube = Youtube()
        if len(html.unescape(video.get('snippet').get('title'))) > 50:
            youtube.title = html.unescape(video.get('snippet').get('title'))[:50] + '...'
        else:
            youtube.title = html.unescape(video.get('snippet').get('title'))
        youtube.description = html.unescape(video.get('snippet').get('description'))
        youtube.video_id = html.unescape(video.get('id').get('videoId'))
        youtube.image_url = html.unescape(video.get('snippet').get('thumbnails').get('high').get('url'))
        youtube.save()
    return Response([])


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news,many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def getnews(request):
    naver_id = settings.naver_ID
    naver_key = settings.naver_KEY
    url = 'https://openapi.naver.com/v1/search/news.json?query=금융&start=1&display=30'
    headers = {'X-Naver-Client-Id':'hA5tn6adwDPQB3ldzXJy','X-Naver-Client-Secret':'xPZUuPw7xe'}
    response = requests.get(url,headers=headers).json()
    # print(response)
    for item in response.get('items'):
        print(item.get('link'))
        if 'news.naver' in item.get('link'):
            news = News()
            news.title = html.unescape(item.get('title')).replace('<b>','').replace('</b>','')
            news.description = html.unescape(item.get('description')).replace('<b>','').replace('</b>','')
            news.naver_url = item.get('link')
            res = requests.get(item.get('link'))
            abc = res.text
            soup = BeautifulSoup(abc, 'html.parser')
            if not soup.select_one('#img1'):
                continue
            if not soup.select_one('#img1').get('data-src'):
                continue
            news.image_url = soup.select_one('#img1').get('data-src')
            news.save()
    return Response({'asd':'asd'})


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def getexchange(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=9TbzRbWuNPvOkkXHBLwKrUDQjvK5wPWY&data=AP01&searchdate=20231116'
    response = requests.get(url).json()
    exchanges = Exchange.objects.all()
    exchanges.delete()
    for excha in response:
        print(excha)
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


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def exchange(request):
    exchanges = Exchange.objects.all()
    serializer = ExchangeSerializer(exchanges, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getindex(requs):
    url = 'https://m.stock.naver.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    temp = soup.select_one('.MajorStockIndexList_inner__Jz7ug').select('.MajorStockIndexList_list___wDhf')
    for el in temp:
        data_list = el.get_text(separator="***").split('***')
        img_url = el.select_one('img').get('src')
        name = data_list[0]
        now_price = data_list[1]
        print(data_list)
        if data_list[3][0] == '-':
            price_raise = '-' + data_list[2]
        else:
            price_raise = '+' + data_list[2]
        price_raise_percent = data_list[3]
        updated_day = data_list[4]
        idx = Index()
        idx.name = name
        idx.now_price = now_price
        idx.chart_url = img_url
        idx.price_raise = price_raise
        idx.price_raise_percent = price_raise_percent
        idx.updated_day = updated_day
        idx.save()
    return Response('생성되었습니다.')


@api_view(['GET'])
def index(request):
    indexs = Index.objects.all()
    serializer = IndexSerializer(indexs, many=True)
    return Response(serializer.data)

type_dic = {
    0 : '코스피',
    1 : '코스닥',
    2 : '나스닥',
    3 : 'S&P500',
}

@api_view(['GET'])
def getstock(request):
    url_list = [
        'https://kr.investing.com/indices/kospi',
        'https://kr.investing.com/indices/kosdaq',
        'https://kr.investing.com/indices/nq-100',
        'https://kr.investing.com/indices/us-spx-500'
    ]
    for i in range(4):
        response = requests.get(url_list[i]).text
        soup = BeautifulSoup(response, "html.parser")
        temp = (soup.select('#__next > div.desktop\:relative.desktop\:bg-background-default > div.relative.flex > div.pt-5.md\:pt-10.xl\:container.xl\:mx-auto.font-sans-v2.antialiased.text-\[\#232526\].grid.grid-cols-1.md\:grid-cols-\[1fr_72px\].lg\:grid-cols-\[1fr_420px\].px-4.sm\:px-6.md\:px-7.md\:gap-6.lg\:px-8.lg\:gap-8.flex-1 > div.min-w-0 > div.flex.flex-col.md\:flex-row.md\:gap-\[50px\] > div'))
        
        table = temp[0].select('tbody > tr')

        for stockdata in table:
            data = stockdata.get_text(separator='***').split('***')
            stock = Stock()
            stock.name = data[1]
            stock.now_price = data[2]
            stock.price_raise = data[3]
            stock.price_raise_percent = data[4]
            stock.is_raise = '급등'
            stock.type = type_dic[i]
            stock.save()
        
        
        table = temp[1].select('tbody > tr')

        for stockdata in table:
            data = stockdata.get_text(separator='***').split('***')
            stock = Stock()
            stock.name = data[1]
            stock.now_price = data[2]
            stock.price_raise = data[3]
            stock.price_raise_percent = data[4]
            stock.is_raise = '급락'
            stock.type = type_dic[i]
            stock.save()

    return Response([])

@api_view(['GET'])
def stock(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)