import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import DepositProduct, DepositOption, SavingProduct, SavingOption, DepositProductList, SavingProductList
from .serializers import DepositProductSerializer, DepositOptionSerializer, SavingProductSerializer, SavingOptionSerializer, DepositProductListSerializer, SavingProductListSerializer

# 정기예금 실행 시 작동
# 금융감독원의 "정기예금" API 로 부터 자료를 수신받아
# 데이터베이스에 저장하고,
# 저장된 데이터베이스를 JSON 형태로 반환
@api_view(['GET'])
def deposit_list(request):
    # API 키
    API_KEY = '58476eeb85a1feef2bd1156e726ce9ae'

    # 금융감독원 정기예금 JSON 요청 API
    URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    
    # JSON 데이터 불러오기
    response = requests.get(URL).json()

    # 예금상품을 DepositProduct 에 저장하기
    for prdt in response.get('result').get('baseList'):

        # 중복값 검사하기
        is_duplicated = False
        for record in DepositProduct.objects.all():
            if record.fin_prdt_cd == prdt.get('fin_prdt_cd'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        prdt_data = {
            'dcls_month': prdt.get('dcls_month'),  
            'fin_co_no': prdt.get('fin_co_no'),               
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'join_way': prdt.get('join_way'),
            'mtrt_int': prdt.get('mtrt_int'),
            'spcl_cnd': prdt.get('spcl_cnd'),
            'join_deny': prdt.get('join_deny'),
            'join_member': prdt.get('join_member'),
            'etc_note': prdt.get('etc_note'),
            'max_limit': prdt.get('max_limit'),
            'dcls_strt_day': prdt.get('dcls_strt_day'),
            'dcls_end_day': prdt.get('dcls_end_day'),
            'fin_co_subm_day': prdt.get('fin_co_subm_day'),
        }

        serializer = DepositProductSerializer(data=prdt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 상품옵션을 DepositOption 에 저장하기
    for opt in response.get('result').get('optionList'):
        
        # 해당 옵션이 속한 상품의 코드
        prdt_cd = opt.get('fin_prdt_cd')

        # 해당 상품 객체 불러오기
        prdt = DepositProduct.objects.get(fin_prdt_cd=prdt_cd)
        
        # 중복값 검사하기
        is_duplicated = False
        for record in DepositOption.objects.all():
            if record.fin_prdt_cd == prdt_cd and record.save_trm == opt.get('save_trm'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        opt_data = {
            'dcls_month': opt.get('dcls_month'),
            'fin_co_no': opt.get('fin_co_no'),
            'fin_prdt_cd': opt.get('fin_prdt_cd'),
            'intr_rate_type': opt.get('intr_rate_type'),
            'intr_rate_type_nm': opt.get('intr_rate_type_nm'),
            'save_trm': opt.get('save_trm'),
            'intr_rate': opt.get('intr_rate'),
            'intr_rate2': opt.get('intr_rate2'),
        }

        serializer = DepositOptionSerializer(data=opt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(depositproduct=prdt)


    # 상품별 이자옵션 기재된 새로운 DB 저장
    # DB에 저장된 각 상품에 대하여
    for product in DepositProduct.objects.all():

        # 중복값 검사하기
        is_duplicated = False
        for record in DepositProductList.objects.all():
            if record.fin_prdt_cd == product.fin_prdt_cd:
                is_duplicated = True
                break
        if is_duplicated:
            continue


        # DB에 저장된 해당 상품의 모든 옵션들 불러오기
        options = product.depositoption_set.all()

        # 6개월, 12개월, 24개월, 36개월 이자 정보를 저장할 인스턴스
        rate_6 = None
        rate_12 = None
        rate_24 = None
        rate_36 = None

        # 기간별로 이자 정보 등록하기
        for option in options:
            period = option.save_trm
            rate1 = option.intr_rate
            rate2 = option.intr_rate2

            if period == '6':
                # null 값을 대비하여 유효성 검사하기
                if rate1:
                    rate_6 = rate1
                else:
                    rate_6 = rate2
            elif period == '12':
                if rate1:
                    rate_12 = rate1
                else:
                    rate_12 = rate2
            elif period == '24':
                if rate1:
                    rate_24 = rate1
                else:
                    rate_24 = rate2
            elif period == '36':
                if rate1:
                    rate_36 = rate1
                else:
                    rate_36 = rate2


        # DB 에 넣을 data 취합하기
        prdt_with_rate = {
            'dcls_month': product.dcls_month,                  
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rate_6': rate_6,
            'rate_12': rate_12,
            'rate_24': rate_24,
            'rate_36': rate_36,
        }

        serializer = DepositProductListSerializer(data=prdt_with_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 프론트로 리스트 데이터 전송하기
    products = get_list_or_404(DepositProductList)
    serializer = DepositProductListSerializer(products, many=True)
    return Response(serializer.data)



#########################################################################################

# 적금 실행 시 작동
# 금융감독원의 "적금" API 로 부터 자료를 수신받아
# 데이터베이스에 저장하고,
# 저장된 데이터베이스를 JSON 형태로 반환
@api_view(['GET'])
def saving_list(request):
    # API 키
    API_KEY = '58476eeb85a1feef2bd1156e726ce9ae'

    # 금융감독원 적금 JSON 요청 API
    URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    
    # JSON 데이터 불러오기
    response = requests.get(URL).json()

    # 적금상품을 SavingProduct 에 저장하기
    for prdt in response.get('result').get('baseList'):

        # 중복값 검사하기
        is_duplicated = False
        for record in SavingProduct.objects.all():
            if record.fin_prdt_cd == prdt.get('fin_prdt_cd'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        prdt_data = {
            'dcls_month': prdt.get('dcls_month'),  
            'fin_co_no': prdt.get('fin_co_no'),               
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'join_way': prdt.get('join_way'),
            'mtrt_int': prdt.get('mtrt_int'),
            'spcl_cnd': prdt.get('spcl_cnd'),
            'join_deny': prdt.get('join_deny'),
            'join_member': prdt.get('join_member'),
            'etc_note': prdt.get('etc_note'),
            'max_limit': prdt.get('max_limit'),
            'dcls_strt_day': prdt.get('dcls_strt_day'),
            'dcls_end_day': prdt.get('dcls_end_day'),
            'fin_co_subm_day': prdt.get('fin_co_subm_day'),
        }

        serializer = SavingProductSerializer(data=prdt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 상품옵션을 SavingOption 에 저장하기
    for opt in response.get('result').get('optionList'):
        
        # 해당 옵션이 속한 상품의 코드
        prdt_cd = opt.get('fin_prdt_cd')

        # 해당 상품 객체 불러오기
        prdt = SavingProduct.objects.get(fin_prdt_cd=prdt_cd)
        
        # 중복값 검사하기
        is_duplicated = False
        for record in SavingOption.objects.all():
            if record.fin_prdt_cd == prdt_cd and record.save_trm == opt.get('save_trm'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        opt_data = {
            'dcls_month': opt.get('dcls_month'),
            'fin_co_no': opt.get('fin_co_no'),
            'fin_prdt_cd': opt.get('fin_prdt_cd'),
            'intr_rate_type': opt.get('intr_rate_type'),
            'intr_rate_type_nm': opt.get('intr_rate_type_nm'),
            'rsrv_type': opt.get('rsrv_type'),
            'rsrv_type_nm': opt.get('rsrv_type_nm'),
            'save_trm': opt.get('save_trm'),
            'intr_rate': opt.get('intr_rate'),
            'intr_rate2': opt.get('intr_rate2'),
        }

        serializer = SavingOptionSerializer(data=opt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(savingproduct=prdt)


    # 상품별 이자옵션 기재된 새로운 DB 저장
    # DB에 저장된 각 상품에 대하여
    for product in SavingProduct.objects.all():

        # 중복값 검사하기
        is_duplicated = False
        for record in SavingProductList.objects.all():
            if record.fin_prdt_cd == product.fin_prdt_cd:
                is_duplicated = True
                break
        if is_duplicated:
            continue


        # DB에 저장된 해당 상품의 모든 옵션들 불러오기
        options = product.savingoption_set.all()

        # 6개월, 12개월, 24개월, 36개월 이자 정보를 저장할 인스턴스
        rate_6 = None
        rate_12 = None
        rate_24 = None
        rate_36 = None

        # 기간별로 이자 정보 등록하기
        for option in options:
            period = option.save_trm
            rate1 = option.intr_rate
            rate2 = option.intr_rate2

            if period == '6':
                # null 값을 대비하여 유효성 검사하기
                if rate1:
                    rate_6 = rate1
                else:
                    rate_6 = rate2
            elif period == '12':
                if rate1:
                    rate_12 = rate1
                else:
                    rate_12 = rate2
            elif period == '24':
                if rate1:
                    rate_24 = rate1
                else:
                    rate_24 = rate2
            elif period == '36':
                if rate1:
                    rate_36 = rate1
                else:
                    rate_36 = rate2


        # DB 에 넣을 data 취합하기
        prdt_with_rate = {
            'dcls_month': product.dcls_month,                  
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rate_6': rate_6,
            'rate_12': rate_12,
            'rate_24': rate_24,
            'rate_36': rate_36,
        }

        serializer = SavingProductListSerializer(data=prdt_with_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 프론트로 리스트 데이터 전송하기
    products = get_list_or_404(SavingProductList)
    serializer = SavingProductListSerializer(products, many=True)
    return Response(serializer.data)


# 예금 상품 상세 데이터 불러오는 view
@api_view(['GET'])
def deposit_detail(request, fin_prdt_cd):
    product = get_object_or_404(DepositProduct, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductSerializer(product)
    return Response(serializer.data)


# 적금 상품 상세 데이터 불러오는 view
@api_view(['GET'])
def saving_detail(request, fin_prdt_cd):
    product = get_object_or_404(SavingProduct, fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductSerializer(product)
    return Response(serializer.data)
