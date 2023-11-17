from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def exchange(request, fromCountry, toCountry, price):
    # 환율 정보 가져오기
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=nJrSIWLxo06igbLUpsy8jF93POiYAzyt&searchdate=20180102&data=AP01'
    requestData = requests.get(URL)
    result = requestData.json()
    
    # 환율 계산
    if fromCountry == 'KRW':
        for data in result:
            if data.get('cur_unit') == toCountry:
                exchange_rate = float(data.get('deal_bas_r').replace(',',''))
                break
        exchangeresult = price / exchange_rate
    else:
        for data in result:
            if data.get('cur_unit') == fromCountry:
                exchange_rate = float(data.get('deal_bas_r').replace(',',''))
                break
        exchangeresult = price * exchange_rate
    exchangeresult = round(exchangeresult , 2)
    return Response({"exchangeresult": exchangeresult})