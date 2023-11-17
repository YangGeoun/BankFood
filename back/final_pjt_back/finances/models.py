from django.db import models

# # Create your models here.
class Deposit(models.Model):
    fin_prdt_cd = models.TextField()                     # fin_prdt_cd 금융상품번호
    fin_prdt_nm = models.TextField()                     # fin_prdt_nm 금융상품명
    kor_co_nm = models.TextField()                       # kor_co_nm   금융회사명
    dcls_month = models.TextField()                      # dcls_month  공시 제출월 [YYYYMM]
    join_deny = models.TextField()                    # join_deny   가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_way = models.TextField()                        # join_way    가입 방법
    spcl_cnd = models.TextField()                        # spcl_cnd    우대조건
    max_limit = models.FloatField(blank=True, null=True) # max_limit   최고한도
    etc_note = models.TextField()                        # etc_note    기타 유의사항


class DepositOption(models.Model):
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()                     # fin_prdt_cd 금융상품번호
    save_trm = models.TextField()                        # save_trm    저축 기간 [단위: 개월]
    intr_rate = models.FloatField()                      # intr_rate   저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                     # intr_rate   최고 우대금리 [소수점 2자리]
    intr_rate_type_nm = models.TextField()                # intr_rate_type_nm  	저축 금리 유형명


class Saving(models.Model):
    fin_prdt_cd = models.TextField()                     # fin_prdt_cd 금융상품번호
    fin_prdt_nm = models.TextField()                     # fin_prdt_nm 금융상품명
    kor_co_nm = models.TextField()                       # kor_co_nm   금융회사명
    dcls_month = models.TextField()                      # dcls_month  공시 제출월 [YYYYMM]
    join_deny = models.TextField()                    # join_deny   가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_way = models.TextField()                        # join_way    가입 방법
    spcl_cnd = models.TextField()                        # spcl_cnd    우대조건
    max_limit = models.FloatField(blank=True, null=True) # max_limit   최고한도
    etc_note = models.TextField()                        # etc_note    기타 유의사항
    mtrt_int = models.TextField()                        # mtrt_int    만기 후 이자율


class SavingOption(models.Model):
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()                     # fin_prdt_cd 금융상품번호
    save_trm = models.TextField()                        # save_trm    저축 기간 [단위: 개월]
    intr_rate = models.FloatField()                      # intr_rate   저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                     # intr_rate   최고 우대금리 [소수점 2자리]
    intr_rate_type_nm = models.TextField()               # intr_rate_type_nm  	저축 금리 유형명
    rsrv_type_nm = models.TextField()                    # rsrv_type_nm         적립 유형명

# class Card(models.Model):



# class Fund(models.Model):
