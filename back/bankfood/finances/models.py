from django.db import models

# Create your models here.
class Deposit(models.Model):
    fin_prdt_nm = models.CharField(max_length=100)       # fin_prdt_nm 금융상품명
    kor_co_nm = models.CharField(max_length=100)         # kor_co_nm   금융회사명
    dcls_month = models.CharField(max_length=10)         # dcls_month  공시 제출월 [YYYYMM]
    join_deny = models.IntegerField()                    # join_deny   가입제한
    join_way = models.CharField(max_length=100)          # join_way    가입 방법
    spcl_cnd = models.TextField()                        # spcl_cnd    우대조건
    max_limit = models.FloatField()                      # max_limit   최고한도
    etc_note = models.TextField()                        # etc_note    기타 유의사항
    # 그냥 금리
    # 최고 우대금리
    # 저축기간
    
    # 옵션?? 이랑 나눠서 참조하게 하기

# class Saving(models.Model):



# class Card(models.Model):



# class Fund(models.Model):

