from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings



@api_view(['GET'])
def exchange(request, fromCountry, toCountry, price, st_date):
    # 환율 정보 가져오기
    API_KEY = settings.CURRENCY_API_KEY
    URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=${API_KEY}&searchdate={st_date}&data=AP01'
    requestData = requests.get(URL)
    result = requestData.json()
    
    exchange_rate=1
    exchangeresult = 1
    # 환율 계산
    for data in result:
        if data.get('cur_unit') == fromCountry:
            exchange_rate = float(data.get('deal_bas_r').replace(',',''))
            print(data.get('deal_bas_r'))
            exchangeresult = price * exchange_rate
            break
    # else:
    #     for data in result:
    #         if data.get('cur_unit') == fromCountry:
    #             exchange_rate = float(data.get('deal_bas_r').replace(',',''))
    #             exchangeresult = price * exchange_rate
    #             break
    exchangeresult = round(exchangeresult , 3)
    return Response({"exchangeresult": exchangeresult})
