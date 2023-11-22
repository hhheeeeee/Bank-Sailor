import random
import requests


# deposit 38개
# saving 50개
# user 10000명





dict_keys = ['depositproductlist_id', 'user_id']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

N = 20
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '../backend/accounts/fixtures/user_data_1.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    for i in range(N):
        file["model"] = "products.depositproductlist"
        file["pk"] = i+1
        file["fields"] = {
            # 'depositproductlist' : [random.randrange(1,38)],
            'like_users': [random.randrange(1,10)],
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')