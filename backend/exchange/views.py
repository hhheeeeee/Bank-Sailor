from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def exchange(request, fromCountry, toCountry, price):
    # 환율 정보 가져오기
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=nJrSIWLxo06igbLUpsy8jF93POiYAzyt&searchdate=20180102&data=AP01'
    requestData = requests.get(URL)
    result = requestData.json()

    # Find exchange rate for fromCountry to KRW
    from_rate = 1.0
    if fromCountry != 'KRW':
        for data in result:
            if data.get('cur_unit') == fromCountry:
                from_rate = float(data.get('deal_bas_r').replace(',', ''))
                if fromCountry == 'JPY(100)' or fromCountry == 'IDR(100)':
                    from_rate /= 100  # 
                break

    # Find exchange rate for toCountry to KRW
    to_rate = 1.0
    for data in result:
        if data.get('cur_unit') == toCountry:
            to_rate = float(data.get('deal_bas_r').replace(',', ''))
            if toCountry == 'JPY(100)' or toCountry == 'IDR(100)':
                to_rate /= 100 
            break

    # Calculate exchange result
    if fromCountry == 'KRW':
        exchangeresult = price / to_rate
    else:
        exchangeresult = price * (to_rate / from_rate)

    exchangeresult = round(exchangeresult, 2)
    print(fromCountry, toCountry, price)
    print('=====================================')

    return Response({"exchangeresult": exchangeresult})
