from django.db import models

# # Create your models here.
# class Deposit(models.Model):
#     fin_prdt_nm = models.CharField(max_length=100)       # fin_prdt_nm 금융상품명
#     kor_co_nm = models.CharField(max_length=100)         # kor_co_nm   금융회사명
#     dcls_month = models.CharField(max_length=10)         # dcls_month  공시 제출월 [YYYYMM]
#     join_deny = models.IntegerField()                    # join_deny   가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
#     join_way = models.CharField(max_length=100)          # join_way    가입 방법
#     spcl_cnd = models.TextField()                        # spcl_cnd    우대조건
#     max_limit = models.FloatField()                      # max_limit   최고한도
#     etc_note = models.TextField()                        # etc_note    기타 유의사항


# class DepositOption(models.Model):  
#     save_trm = models.TextField()                        # save_trm    저축 기간 [단위: 개월]
#     intr_rate = models.FloatField()                      # intr_rate   저축 금리 [소수점 2자리]
#     intr_rate2 = models.FloatField()                     # intr_rate   최고 우대금리 [소수점 2자리]
#     intr_rate_type_nm = models.CharField(max_length=10)  # intr_rate_type_nm  	저축 금리 유형명


# class Saving(models.Model):
#     fin_prdt_nm = models.CharField(max_length=100)       # fin_prdt_nm 금융상품명
#     kor_co_nm = models.CharField(max_length=100)         # kor_co_nm   금융회사명
#     dcls_month = models.CharField(max_length=10)         # dcls_month  공시 제출월 [YYYYMM]
#     join_deny = models.IntegerField()                    # join_deny   가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
#     join_way = models.TextField(max_length=100)          # join_way    가입 방법
#     spcl_cnd = models.TextField()                        # spcl_cnd    우대조건
#     max_limit = models.FloatField()                      # max_limit   최고한도
#     etc_note = models.TextField()                        # etc_note    기타 유의사항
#     mtrt_int = models.TextField()                        # mtrt_int    만기 후 이자율


# class SavingOption(models.Model):  

#     save_trm = models.TextField()                        # save_trm    저축 기간 [단위: 개월]
#     intr_rate = models.FloatField()                      # intr_rate   저축 금리 [소수점 2자리]
#     intr_rate2 = models.FloatField()                     # intr_rate   최고 우대금리 [소수점 2자리]
#     intr_rate_type_nm = models.CharField(max_length=10)  # intr_rate_type_nm  	저축 금리 유형명
#     rsrv_type_nm = models.CharField(max_length=10)       # rsrv_type_nm         적립 유형명

# # class Card(models.Model):



# # class Fund(models.Model):
