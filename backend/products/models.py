from django.db import models


# 정기예금 상품 테이블
class DepositProduct(models.Model):
    dcls_month = models.CharField(max_length=50)   
    fin_co_no = models.CharField(max_length=50)                 
    fin_prdt_cd = models.CharField(max_length=50, unique=True)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField()
    dcls_strt_day = models.CharField(max_length=50)
    dcls_end_day = models.CharField(max_length=50)
    fin_co_subm_day = models.CharField(max_length=50)


# 정기예금 옵션 테이블
class DepositOption(models.Model):
    # 상품참조할 외래키 설정
    depositproduct = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    
    dcls_month = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=50)
    fin_prdt_cd = models.CharField(max_length=50)
    intr_rate_type = models.CharField(max_length=50)
    intr_rate_type_nm = models.CharField(max_length=50)
    save_trm = models.CharField(max_length=50)
    intr_rate = models.IntegerField()
    intr_rate2 = models.IntegerField()


# 정기적금 상품 테이블
class SavingProduct(models.Model):
    dcls_month = models.CharField(max_length=50)   
    fin_co_no = models.CharField(max_length=50)                 
    fin_prdt_cd = models.CharField(max_length=50, unique=True)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField()
    dcls_strt_day = models.CharField(max_length=50)
    dcls_end_day = models.CharField(max_length=50)
    fin_co_subm_day = models.CharField(max_length=50)


# 정기적금 옵션 테이블
class SavingOption(models.Model):
    # 상품참조할 외래키 설정
    savingproduct = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    
    dcls_month = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=50)
    fin_prdt_cd = models.CharField(max_length=50)
    intr_rate_type = models.CharField(max_length=50)
    intr_rate_type_nm = models.CharField(max_length=50)
    rsrv_type = models.CharField(max_length=50)
    rsrv_type_nm = models.CharField(max_length=50)
    save_trm = models.CharField(max_length=50)
    intr_rate = models.IntegerField()
    intr_rate2 = models.IntegerField()