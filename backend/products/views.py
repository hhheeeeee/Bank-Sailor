import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import DepositProduct, DepositOption, SavingProduct, SavingOption, DepositProductList, SavingProductList
from .serializers import DepositProductSerializer, DepositOptionSerializer, SavingProductSerializer, SavingOptionSerializer, DepositProductListSerializer, SavingProductListSerializer,DepositProductListSerializer1, SavingProductListSerializer1
from accounts.models import User
from django.core.mail import send_mail

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors


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
        rate_6_max = None
        rate_12 = None
        rate_12_max = None
        rate_24 = None
        rate_24_max = None
        rate_36 = None
        rate_36_max = None

        # 기간별로 이자 정보 등록하기
        for option in options:
            period = option.save_trm
            rate1 = option.intr_rate
            rate2 = option.intr_rate2

            if period == '6':
                rate_6 = rate1
                rate_6_max = rate2
            elif period == '12':
                rate_12 = rate1
                rate_12_max = rate2
            elif period == '24':
                rate_24 = rate1
                rate_24_max = rate2
            elif period == '36':
                rate_36 = rate1
                rate_36_max = rate2


        # DB 에 넣을 data 취합하기
        prdt_with_rate = {
            'dcls_month': product.dcls_month,                  
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rate_6': rate_6,
            'rate_6_max': rate_6_max,
            'rate_12': rate_12,
            'rate_12_max': rate_12_max,
            'rate_24': rate_24,
            'rate_24_max': rate_24_max,
            'rate_36': rate_36,
            'rate_36_max': rate_36_max,
        }

        serializer = DepositProductListSerializer(data=prdt_with_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 프론트로 리스트 데이터 전송하기
    products = get_list_or_404(DepositProductList)
    serializer = DepositProductListSerializer(products, many=True)

    return Response(serializer.data)


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
        rate_6_max = None
        rate_12 = None
        rate_12_max = None
        rate_24 = None
        rate_24_max = None
        rate_36 = None
        rate_36_max = None

        # 기간별로 이자 정보 등록하기
        for option in options:
            period = option.save_trm
            rate1 = option.intr_rate
            rate2 = option.intr_rate2

            if period == '6':
                rate_6 = rate1
                rate_6_max = rate2
            elif period == '12':
                rate_12 = rate1
                rate_12_max = rate2
            elif period == '24':
                rate_24 = rate1
                rate_24_max = rate2
            elif period == '36':
                rate_36 = rate1
                rate_36_max = rate2


        # DB 에 넣을 data 취합하기
        prdt_with_rate = {
            'dcls_month': product.dcls_month,                  
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rate_6': rate_6,
            'rate_6_max': rate_6_max,
            'rate_12': rate_12,
            'rate_12_max': rate_12_max,
            'rate_24': rate_24,
            'rate_24_max': rate_24_max,
            'rate_36': rate_36,
            'rate_36_max': rate_36_max,
        }

        serializer = SavingProductListSerializer(data=prdt_with_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 프론트로 리스트 데이터 전송하기
    products = get_list_or_404(SavingProductList)
    serializer = SavingProductListSerializer(products, many=True)
    return Response(serializer.data)


# 예금 상품 상세 데이터 불러오는 view
# POST 요청일 경우, 해당 상세 상품을 로그인한 유저 계정의 financial_products 필드에 추가
@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deposit_detail(request, fin_prdt_cd):
    # 상품 상세 정보 보기
    if request.method == 'GET':
        product = get_object_or_404(DepositProduct, fin_prdt_cd=fin_prdt_cd)
        serializer = DepositProductSerializer(product)
        return Response(serializer.data)
    
    # 해당 상품 가입하기
    elif request.method == 'POST':
        # 유저정보 불러오기
        deposit = DepositProductList.objects.get(fin_prdt_cd=fin_prdt_cd)
        if request.user in deposit.like_users.all():
            return Response(status=status.HTTP_409_CONFLICT)
            
        else:
            deposit.like_users.add(request.user)
            return Response(status=status.HTTP_200_OK)


    # 해당 상품 금리 수정하기
    elif request.method == 'PUT':
        # 전달받은 신규 금리
        new_rate = request.data.get('rate')     # 신규 금리
        rateType = request.data.get('rateType') # 금리 타입
        
        option = DepositOption.objects.get(fin_prdt_cd=fin_prdt_cd, save_trm=rateType)
        
        list_new_rate = DepositProductList.objects.get(fin_prdt_cd=fin_prdt_cd)

        serializer1 = DepositOptionSerializer(option, data={'intr_rate': new_rate}, partial=True)
        serializer2 = DepositProductListSerializer(list_new_rate, data={f'rate_{rateType}': new_rate}, partial=True)

        if serializer1.is_valid() and serializer2.is_valid():
            serializer1.save()
            serializer2.save()
            return Response({"message": "true"})
        else:
            return Response({"message": "false"})



# 적금 상품 상세 데이터 불러오는 view
@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def saving_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        product = get_object_or_404(SavingProduct, fin_prdt_cd=fin_prdt_cd)
        serializer = SavingProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # 유저정보 불러오기
        saving = SavingProductList.objects.get(fin_prdt_cd=fin_prdt_cd)
        if request.user in saving.like_users.all():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            saving.like_users.add(request.user)
            return Response(status=status.HTTP_200_OK)

    # 해당 상품 금리 수정하기
    elif request.method == 'PUT':
        # 전달받은 신규 금리
        new_rate = request.data.get('rate')     # 신규 금리
        rateType = request.data.get('rateType') # 금리 타입


        option = SavingOption.objects.get(fin_prdt_cd=fin_prdt_cd, save_trm=rateType)
        

        list_new_rate = SavingProductList.objects.get(fin_prdt_cd=fin_prdt_cd)

        serializer1 = SavingOptionSerializer(option, data={'intr_rate': new_rate}, partial=True)
        serializer2 = SavingProductListSerializer(list_new_rate, data={f'rate_{rateType}': new_rate}, partial=True)

        if serializer1.is_valid() and serializer2.is_valid():
            serializer1.save()
            serializer2.save()
            return Response({"message": "true"})
        else:
            return Response({"message": "false"})



# 금리 변동 시 이메일 발송
@api_view(['GET'])
def send_email_on_change(request):
    # 상품코드, 기존금리, 변경금리 받아온 것
    prdt_code = request.GET.get('prdtCode')
    old_rate = request.GET.get('oldRate')
    new_rate = request.GET.get('newRate')
    period = request.GET.get('period')


    try:
        product = DepositProductList.objects.get(fin_prdt_cd=prdt_code)
    except:
        product = SavingProductList.objects.get(fin_prdt_cd=prdt_code)
    

    # 해당 상품명
    prdt_name = product.fin_prdt_nm


    # 해당 상품 가입한 유저들 이메일 수집하기
    to = []     # 이메일 목록

    for user in product.like_users.all():
        to.append(user.email)


    # 이메일 내용
    title = '[BankSailor] 가입하신 상품의 금리정보가 변동되어 안내드립니다'
    content = f'안녕하세요 고객님, 가입하신 {prdt_name} 상품의 금리정보가 변동되어 안내드립니다.\n\n금리옵션: {period}개월\n변동 전 금리: {old_rate}%\n변동 후 금리: {new_rate}%'
    
    # 이메일 보내기
    send_mail(
        title,
        content,
        'xorms5712@naver.com',
        to,
    )


    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def recommend(request):
    if request.method == 'POST':

        USERPK = request.user.pk

        # 1. age, salary, money 비슷한 유저들 뽑고 그 유저들은 뭐 쓰는지 보여주기
        data = User.objects.all()
        data_list = list(data.values('id', 'money', 'age', 'salary'))
        df = pd.DataFrame.from_records(data_list)
        # index를 id로 지정
        df.set_index('id', inplace=True)
        # 사용할 특성 선택
        features = ['age', 'money', 'salary']
        # 특성 스케일링
        scaler = StandardScaler()
        df[features] = scaler.fit_transform(df[features]) 

        # Find the features of the current user
        user_data = df.loc[USERPK].values.reshape(1, -1)

        # KNN 모델 생성
        knn_model = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
        knn_model.fit(df[features])

        # Find the nearest neighbors based on the features of the current user
        distances, indices = knn_model.kneighbors(user_data)

        # 가장 가까운 이웃의 인덱스를 이용하여 pk(id) 값을 가져오기
        closest_neighbors_ids = df.index[indices[0]]

        # 결과 출력
        print("가장 가까운 이웃의 pk(id) 값:", closest_neighbors_ids)

        recommend_deposit = []
        recommend_saving = []
        myassets = []
        nowuser = User.objects.get(pk=request.user.pk)
        now_user_liked_deposits = nowuser.like_deposit.all()
        now_user_liked_savings = nowuser.like_saving.all()
        for id in closest_neighbors_ids:
            if id != USERPK:
                other_user = User.objects.get(pk=id)
                other_user_liked_deposits = other_user.like_deposit.all()
                other_user_liked_savings = other_user.like_saving.all()
                for d in other_user_liked_deposits:
                    if d not in now_user_liked_deposits:
                        recommend_deposit.append(d)
                for s in other_user_liked_savings:
                    if s not in now_user_liked_savings:
                        recommend_saving.append(s)
        deposit_serializer = DepositProductListSerializer(recommend_deposit, many=True)
        saving_serializer = SavingProductListSerializer(recommend_saving, many=True)

        serialized_data = {
            'deposits': deposit_serializer.data,
            'savings' : saving_serializer.data
        }
        print(serialized_data)
        return Response(serialized_data)
