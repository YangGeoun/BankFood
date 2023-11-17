import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.conf import settings
from .models import Deposit, DepositOption, Saving, SavingOption

# Create your views here.

join_deny_dic = { '1' : '제한없음', '2' : '서민전용', '3': '일부제한'}


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