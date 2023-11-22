
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Deposit, DepositOption, Saving, SavingOption, Card, Fund
from .serializer import DepositSerializer, SavingSerializer, CardSerializer, FundSerializer

# Create your views here.

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

@api_view(['GET'])
def aaa(requser):
    User = get_user_model()
    
    df = pd.DataFrame(
    list(
        User.objects.all().values(
            'id','age','salary', 'money','gender'
        )
    )
    )
   
    normalization_df = (df - df.min())/(df.max() - df.min())
    user_sim = cosine_similarity(normalization_df, normalization_df)
    user_sim_df = pd.DataFrame(user_sim, index=normalization_df.id, columns=normalization_df.id)
    print(user_sim_df)
    print(df['gender'])
    return Response({'ad':'asd'})





join_deny_dic = { '1' : '제한없음', '2' : '서민전용', '3': '일부제한'}
benefits_dic = {
    '주유': 'fuel',
    '쇼핑' : 'shoping',
    '대형마트' : 'supermarket',
    '편의점': 'convenience_store',
    '외식' : 'eat_out',
    '카페/베이커리' : 'cafe_bakery',
    '영화' : 'movie',
    '대중교통' : 'public_transport',
    '관리비' : 'maintenance',
    '통신' : 'communication',
    '교육' : 'education',
    '육아' : 'parenting',
    '문화' : 'culture',
    '레저' : 'leisure',
    '항공마일리지' : 'airline_mileage',
    '프리미엄' : 'premium',
    '하이패스' : 'hi_pass',
    '오토' : 'auto',
    '의료' : 'medical',
    '뷰티' : 'beauty',
    '포인트/캐시백' : 'points_cashback',
    '간편결제' : 'easy_payment',
    '렌탈' : 'rental',
    '반려동물' : 'pet',
}

risk_dic = {
    '매우 높은 위험' : 5,
    '높은 위험' : 4,
    '다소 높은 위험' : 3,
    '보통 위험' : 2,
    '낮은 위험': 1,
    '매우 낮은 위험' : 0
}

@api_view(['GET'])
def deposit(request):
    deposits = Deposit.objects.all()
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getdeposit(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?topFinGrpNo=020000&pageNo=1&auth=c9c8354f95e8ddb8e192c5bc0859e8bf'
    response = requests.get(url).json()
    for product in response.get('result').get('baseList'):
        if not Deposit.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd')).exists():
            deposit = Deposit()
            deposit.fin_prdt_cd = product.get('fin_prdt_cd')
            deposit.fin_prdt_nm = product.get('fin_prdt_nm')
            deposit.kor_co_nm = product.get('kor_co_nm')
            deposit.dcls_month = product.get('dcls_month')
            deposit.join_deny = join_deny_dic[product.get('join_deny')]
            deposit.join_way = product.get('join_way')
            deposit.spcl_cnd = product.get('spcl_cnd')
            deposit.max_limit = product.get('max_limit')
            deposit.etc_note = product.get('etc_note')
            deposit.save()
    return Response({'asd':'asd'})


@api_view(['GET'])
def saving(request):
    savings = Saving.objects.all()
    serializer = SavingSerializer(savings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getdeopsitoption(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?topFinGrpNo=020000&pageNo=1&auth=c9c8354f95e8ddb8e192c5bc0859e8bf'
    response = requests.get(url).json()
    for option in response.get('result').get('optionList'):
        if not DepositOption.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd'),save_trm=option.get('save_trm')).exists():
        # if not DepositOption.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd')).filer(save_trm=option.get('save_trm')).exists():
            deposit = Deposit.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
            depositoption = DepositOption()
            depositoption.deposit = deposit
            depositoption.fin_prdt_cd = option.get('fin_prdt_cd')
            depositoption.save_trm = option.get('save_trm')
            depositoption.intr_rate = option.get('intr_rate') or 0
            depositoption.intr_rate2 = option.get('intr_rate2')
            depositoption.intr_rate_type_nm = option.get('intr_rate_type_nm')
            depositoption.save()
    return Response({'123':'123'})


@api_view(['GET'])
def getsaving(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth=c9c8354f95e8ddb8e192c5bc0859e8bf&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for product in response.get('result').get('baseList'):
        if not Saving.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd')).exists():
            saving = Saving()
            saving.fin_prdt_cd = product.get('fin_prdt_cd')
            saving.fin_prdt_nm = product.get('fin_prdt_nm')
            saving.kor_co_nm = product.get('kor_co_nm')
            saving.dcls_month = product.get('dcls_month')
            saving.join_deny = join_deny_dic[product.get('join_deny')]
            saving.join_way = product.get('join_way')
            saving.spcl_cnd = product.get('spcl_cnd')
            saving.max_limit = product.get('max_limit')
            saving.etc_note = product.get('etc_note')
            saving.mtrt_int = product.get('mtrt_int')
            saving.save()
    return Response({'asd':'asd'})


@api_view(['GET'])
def getsavingoption(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth=c9c8354f95e8ddb8e192c5bc0859e8bf&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for option in response.get('result').get('optionList'):
        print(option)
        if not SavingOption.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd'),save_trm=option.get('save_trm')).exists():
        # if not DepositOption.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd')).filer(save_trm=option.get('save_trm')).exists():
            saving = Saving.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
            savingoption = SavingOption()
            savingoption.saving = saving
            savingoption.fin_prdt_cd = option.get('fin_prdt_cd')
            savingoption.save_trm = option.get('save_trm')
            savingoption.intr_rate = option.get('intr_rate') or 0
            savingoption.intr_rate2 = option.get('intr_rate2')
            savingoption.intr_rate_type_nm = option.get('intr_rate_type_nm')
            savingoption.rsrv_type_nm = option.get('rsrv_type_nm')
            savingoption.save()
    return Response({'123':'123'})

@api_view(['GET'])
def getcard(request):
    card_id_lst = ['10252', '2552', '10285', '3756', '1153', '2225', '1465', '1408', '1418', '10005', '2337', '3637', '2423', '1030', '3856', '10112', '1530', '10117', '115', '10141', '3456', '1692', '10113', '3578', '10056', '10215', '10152', '1571', '1322', '10221', '1772', '10105', '10267', '2484', '10053', '2917', '10047', '10050', '10290', '10102', '10070', '10103', '2348', '10254', '3996', '1260', '1698', '10071', '160', '3776', '10035', '4047', '10051', '1385', '710', '2486', '1614', '1292', '1768', '10270', '10245', '10288', '2332', '2797', '10045', '2776', '99', '10225', '1400', '10011', '1773', '1361', '10009', '1681', '10039', '1316', '2533', '10121', '3796', '10128', '10236', '247', '2206', '3857', '3717', '1715', '1684', '10214', '10293', '10037', '10219', '3059', '10100', '3798', '1531', '2571', '10143', '1570', '10176', '2471', '10007', '10142', '10046', '3881', '10260', '3277', '2697', '4016', '10179', '10122', '1470', '593', '10201', '1577', '10151', '1243', '3638', '2418', '10052', '2226', '3957', '3959', '1695', '10184', '2185', '10234', '10126', '10108', '10058', '3676', '2487', '2489', '10281', '3977', '10268', '10106', '10107', '10157', '2339', '2532', '1573', '2472', '10297', '10279', '2756', '2956', '4096', '10093', '3816', '10241', '10289', '2483', '3777', '1680', '652', '10154', '10200', '10146', '10124', '3797', '10033', '10118', '10287', '1591', '10049', '3658', '2836', '3196', '2696', '10286', '10029', '10134', '10258', '2857', '2349', '205', '10187', '277', '10226', '10156', '10280', '10144', '2856', '10145', '253', '3378', '3251', '3237', '10064', '10140', '10098', '10269', '10294', '10130', '2422', '10080', '10237', '2886', '3055', '10220', '10096', '2885', '3896', '3877', '2511', '10276', '10218', '2345', '10076', '10223', '3958', '10181', '10246', '10227', '3436', '3836', '10284', '10068', '10135', '2676', '10066', '3937', '10207', '4038', '3337', '3356', '2916', '10072', '2005', '3257', '3339', '3716', '10212', '10186', '10114', '10202', '10264', '1388', '2778', '10185', '1202', '10160', '10256', '10291', '1384', '10235', '10275', '2414', '1362', '2491', '10013', '10189', '1597', '10015', '1157', '3636', '2392', '4048', '10193', '10262', '1825', '2343', '3258', '3556', '4044', '2716', '1360', '10239', '10198', '10164', '10057', '1340', '10197', '10271', '2976', '10132', '10233', '10199', '1158', '1889', '10282', '10300', '2350', '2779', '10097', '10211', '10261', '10232', '2717', '10043', '10213', '10277', '2888', '3616', '3799', '3936', '10138', '1342', '1337', '2419', '3878', '10278', '1826', '3076', '3276', '2490', '10250', '10265', '3736', '10062', '10248', '10249', '10266', '3176', '3178', '10059', '10204', '10247', '1203', '3177', '10203', '10283', '10299']
    for id in card_id_lst:
        url = f'https://card-search.naver.com/item?cardAdId={id}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        card = Card()
        card.name = soup.select_one('.txt').get_text()
        card.naver_card_id = id
        card.annual_fee = soup.select_one('.as_annualFee').select_one('span').get_text()
        card.base_performance = soup.select_one('.as_baseRecord').select_one('span').get_text()

        a = soup.select("summary .name")
        for el in a:
            setattr(card, benefits_dic.setdefault(el.select_one('b').get_text(),'a'), el.select_one('i').get_text())
            print(el.select_one('b').get_text())
            print(el.select_one('i').get_text())
            card.save()


@api_view(['GET'])
def card(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getfund(request):
    url = 'https://www.fundguide.net/Fund/SimpleSearch'

    driver = webdriver.Chrome()
    driver.get(url)

    # 분류목록을 보이게하는 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="btnSchResult"]').click()
    time.sleep(1)

    # 열린 페이지 소스를 받아오기
    for i in range(242):
        html = driver.page_source

        fund1 = Fund()
        fund2 = Fund()
        fund3 = Fund()
        fund4 = Fund()
        fund5 = Fund()
        fund6 = Fund()
        fund7 = Fund()
        fund8 = Fund()
        fund9 = Fund()
        fund10 = Fund()
        lst = [fund1,fund2,fund3,fund4,fund5,fund6,fund7,fund8,fund9,fund10]
        
        # 필요한 정보 파싱
        soup = BeautifulSoup(html, "html.parser")
        table = soup.select_one('#Grid')
        punds = table.select('#resultList > tr')
        
        for i in range(10):
            tds = punds[i].select('td')
            # print(tds[1].select_one('a > span').get_text())    # name
            # print(tds[3].get_text().split('(')[0])  # scale
            # print(tds[4].get_text())                # set date
            # print(tds[5].get_text())                # reword
            # print(tds[8].get_text())                # 3m
            # print(tds[9].get_text())                # 6m
            # print(tds[10].get_text())               # 1y
            # print(tds[11].get_text())               # 3y
            # print(punds[i].select_one('.chart--danger > p').get_text())   # 위험도
            # if punds[i].select_one('.hashtag > span'):    # 키워드
            #     print(punds[i].select_one('.hashtag > span').get_text())
            lst[i].name = tds[1].select_one('a > span').get_text()
            lst[i].operation_scale = tds[3].get_text().split('(')[0].replace(',','')
            lst[i].set_date = tds[4].get_text()
            if tds[5].get_text() != '-':
                lst[i].total_reward = tds[5].get_text().replace(',','')
            if tds[8].get_text() != '-':
                lst[i].revenue_3m = tds[8].get_text().replace(',','')
            if tds[9].get_text() != '-':
                lst[i].revenue_6m = tds[9].get_text().replace(',','')
            if tds[10].get_text() != '-':
                lst[i].revenue_1y = tds[10].get_text().replace(',','')
            if tds[11].get_text() != '-':
                lst[i].revenue_3y = tds[11].get_text().replace(',','')
            lst[i].risk_level = risk_dic[punds[i].select_one('.chart--danger > p').get_text()]
            if punds[i].select_one('.hashtag > span'):
                lst[i].keyword = punds[i].select_one('.hashtag > span').get_text()
            lst[i].save()
        driver.find_element(By.XPATH, '//*[@id="tabPaging"]/div/tr/button[12]').click()
        time.sleep(3)
    return Response({'asd': 'asd'})


@api_view(['GET'])
def fund(request):
    funds = Fund.objects.all()
    serializer = FundSerializer(funds, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def test(request):
    conditions = request.GET
    cards = Card.objects.all()
    if conditions.get('medical') == '1':
        cards = cards.filter(medical__isnull=False)
    if conditions.get('medical') == '2':
        cards = cards.filter(medical__isnull=True)
    if conditions.get('cafe') == '1':
        cards = cards.filter(cafe_bakery__isnull=False)
    if conditions.get('cafe') == '2':
        cards = cards.filter(cafe_bakery__isnull=True)
    if conditions.get('simple_payment') == '1':
        cards = cards.filter(easy_payment__isnull=False)
    if conditions.get('simple_payment') == '2':
        cards = cards.filter(easy_payment__isnull=True)
    if conditions.get('supermaket') == '1':
        cards = cards.filter(supermarket__isnull=False)
    if conditions.get('supermaket') == '2':
        cards = cards.filter(convenience_store__isnull=False)
    if conditions.get('car') == '1':
        cards = cards.filter(fuel__isnull=False)
    if conditions.get('car') == '2':
        cards = cards.filter(public_transport__isnull=False)
    if conditions.get('simple_payment') == '1':
        cards = cards.filter(easy_payment__isnull=False)
    if conditions.get('simple_payment') == '2':
        cards = cards.filter(easy_payment__isnull=True)
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def test(request):
    conditions = request.GET
    funds = Fund.objects.all()
    if conditions.get('medical') == '1':
        cards = cards.filter(medical__isnull=False)
    if conditions.get('medical') == '2':
        cards = cards.filter(medical__isnull=True)
    serializer = FundSerializer(funds, many=True)
    return Response(serializer.data)

banks_list = [
  "경남은행", "광주은행", "국민은행", "농협은행주식회사", "대구은행", "부산은행", "수협은행",
  "신한은행", "우리은행", "전북은행", "제주은행", "주식회사카카오뱅크", "주식회사케이뱅크", 
  "중소기업은행", "토스뱅크주식회사", "하나은행", "한국산업은행", "한국스탠다드차타드은행" 
]

@api_view(['GET'])
def search_deposit(request,bank,type,term):
    print(bank)
    print(type)
    print(term)
    deposits = []
    for i in range(len(bank)):
        if bank[i] == '1':
            for el in Deposit.objects.filter(kor_co_nm=banks_list[i]):
                if term != '0':
                    for option in  el.depositoption_set.all():
                        if option.save_trm == term:
                            if type == '0':
                                deposits.append(el)
                            elif type == '1':
                                if option.intr_rate_type_nm == '단리':
                                    deposits.append(el)
                            elif type == '2':
                                if option.intr_rate_type_nm == '복리':
                                    deposits.append(el)
                else:
                    if type == '0':
                        deposits.append(el)
                    elif type == '1':
                        if el.depositoption_set.all()[0].intr_rate_type_nm == '단리':
                            deposits.append(el)
                    elif type == '2':
                        if el.depositoption_set.all()[0].intr_rate_type_nm == '복리':
                            deposits.append(el)
    serializer = DepositSerializer(deposits,many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def search_saving(request,bank,type,term):
    saving = []
    for i in range(len(bank)):
        if bank[i] == '1':
            for el in Saving.objects.filter(kor_co_nm=banks_list[i]):
                if term != '0':
                    for option in  el.savingoption_set.all():
                        if option.save_trm == term:
                            if type == '0':
                                saving.append(el)
                            elif type == '1':
                                if option.intr_rate_type_nm == '단리':
                                    saving.append(el)
                            elif type == '2':
                                if option.intr_rate_type_nm == '복리':
                                    saving.append(el)
                else:
                    if type == '0':
                        saving.append(el)
                    elif type == '1':
                        if el.savingoption_set.all()[0].intr_rate_type_nm == '단리':
                            saving.append(el)
                    elif type == '2':
                        if el.depositoption_set.all()[0].intr_rate_type_nm == '복리':
                            saving.append(el)
    serializer = SavingSerializer(saving,many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def saving_join(request):
    saving = Saving.objects.filter(fin_prdt_nm=request.data.get('fin_prdt_nm'))
    saving[0].user.add(request.user)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def deposit_join(request):
    deposit = Deposit.objects.filter(fin_prdt_nm=request.data.get('fin_prdt_nm'))
    deposit[0].user.add(request.user)
    return Response(status=status.HTTP_200_OK)



