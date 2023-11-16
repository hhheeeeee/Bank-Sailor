from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
import requests


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

    response = requests.get(URL).json()

    # DepositProduct 에 저장하기
    for prdt in response.get('result').get('baseList'):

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


    
    
    
    
    
    return Response(response)
        

@api_view(['GET'])
def saving_list(request):
    if request.method == 'GET':
        API_KEY = '58476eeb85a1feef2bd1156e726ce9ae'
        URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

        response = requests.get(URL).json()

        return Response(response)