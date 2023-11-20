from django.db import models
from django.conf import settings

# # Create your models here.
class Deposit(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    fin_prdt_cd = models.TextField()                     # fin_prdt_cd 금융상품번호
    fin_prdt_nm = models.TextField()                     # fin_prdt_nm 금융상품명
    kor_co_nm = models.TextField()                       # kor_co_nm   금융회사명
    dcls_month = models.TextField()                      # dcls_month  공시 제출월 [YYYYMM]
    join_deny = models.TextField()                       # join_deny   가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
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
    intr_rate_type_nm = models.TextField()               # intr_rate_type_nm  	저축 금리 유형명


class Saving(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    fin_prdt_cd = models.TextField()                     # fin_prdt_cd 금융상품번호
    fin_prdt_nm = models.TextField()                     # fin_prdt_nm 금융상품명
    kor_co_nm = models.TextField()                       # kor_co_nm   금융회사명
    dcls_month = models.TextField()                      # dcls_month  공시 제출월 [YYYYMM]
    join_deny = models.TextField()                       # join_deny   가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
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


benefits_dic = {
    '주유': 'fuel',
    '쇼핑' : 'shoping',
    '대형마트' : 'supermarket',
    '편의점': 'convenience_store',
    '외식' : 'eat_out',
    '카페/베이커리' : 'cafe/bakery',
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
    '하이패스' : 'hi-pass',
    '오토' : 'auto',
    '의료' : 'medical',
    '뷰티' : 'beauty',
    '포인트/캐시백' : 'points/cashback',
    '간편결제' : 'easy_payment',
    '렌탈' : 'rental',
    '반려동물' : 'pet',
}

# naver_link = f'https://card-search.naver.com/item?cardAdId={naver_card_id}'
class Card(models.Model):
    name = models.TextField() 
    naver_card_id = models.TextField() 
    annual_fee = models.TextField()             # 연회비
    base_performance = models.TextField()      # 기준 실적 (전월 실적)
    # 해택 필드
    fuel = models.TextField(blank=True, null=True) 
    shoping = models.TextField(blank=True, null=True) 
    supermarket = models.TextField(blank=True, null=True) 
    convenience_store = models.TextField(blank=True, null=True) 
    eat_out = models.TextField(blank=True, null=True) 
    cafe_bakery = models.TextField(blank=True, null=True) 
    movie = models.TextField(blank=True, null=True) 
    public_transport = models.TextField(blank=True, null=True) 
    maintenance = models.TextField(blank=True, null=True) 
    communication = models.TextField(blank=True, null=True) 
    education = models.TextField(blank=True, null=True) 
    parenting = models.TextField(blank=True, null=True) 
    culture = models.TextField(blank=True, null=True) 
    leisure = models.TextField(blank=True, null=True) 
    airline_mileage = models.TextField(blank=True, null=True) 
    premium = models.TextField(blank=True, null=True) 
    hi_pass = models.TextField(blank=True, null=True) 
    auto = models.TextField(blank=True, null=True) 
    medical = models.TextField(blank=True, null=True) 
    beauty = models.TextField(blank=True, null=True) 
    points_cashback = models.TextField(blank=True, null=True) 
    easy_payment = models.TextField(blank=True, null=True) 
    rental = models.TextField(blank=True, null=True) 
    pet = models.TextField(blank=True, null=True) 


class Fund(models.Model):
    name = models.TextField()             # 이름
    operation_scale = models.FloatField() # 운영규모
    set_date = models.TextField()         # 설정일
    total_reward = models.FloatField(blank=True, null=True)    # 총보수 (%)
    revenue_3m = models.FloatField(blank=True, null=True)      # 3개월 수익률
    revenue_6m = models.FloatField(blank=True, null=True)      # 6개월 수익률
    revenue_1y = models.FloatField(blank=True, null=True)      # 1년 수익률
    revenue_3y = models.FloatField(blank=True, null=True)      # 3년 수익률
    risk_level = models.IntegerField()    # 1매우 낮음, 2낮음, 3보통, 4위험, 5매우위험
    keyword = models.TextField(blank=True, null=True)       # 키워드