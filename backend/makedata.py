import random
import requests
import json
from collections import OrderedDict

from accounts.models import User
from products.models import DepositProductList, SavingProductList

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"

def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

# 가상의 사용자 데이터 생성
user_data = []

N = 20  # 생성할 가상 사용자 수
i = 0

for i in range(N):
    user = User.objects.create(
        username=str(i) + '이름이라네',
        age=random.randint(1, 100),
        money=random.randrange(0, 100000000, 100000),
        salary=random.randrange(0, 1500000000, 1000000),
        password="1234",
        nickname=None,
        is_active=True,
        is_staff=False,
        is_superuser=False
    )
    # 랜덤하게 상품에 가입된 사용자 생성
    for _ in range(random.randint(1, 5)):
        deposit_product = random.choice(DepositProductList.objects.all())
        saving_product = random.choice(SavingProductList.objects.all())
        deposit_product.like_users.add(user)
        saving_product.like_users.add(user)
    user_data.append(user)

print(f'가상의 사용자 데이터 생성 완료')

# # 생성된 가상 사용자 데이터를 fixture 파일로 저장
# fixture_data = []
# for idx, user in enumerate(user_data, start=1):
#     fixture_data.append({
#         "model": "accounts.User",
#         "pk": idx,
#         "fields": {
#             "username": user.username,
#             "age": user.age,
#             "money": user.money,
#             "salary": user.salary,
#             "password": "1234",
#             "nickname": None,
#             "is_active": user.is_active,
#             "is_staff": user.is_staff,
#             "is_superuser": user.is_superuser
#         }
#     })

# fixture_file_path = '../backend/accounts/fixtures/user_data.json'
# with open(fixture_file_path, 'w', encoding="utf-8") as f:
#     json.dump(fixture_data, f, ensure_ascii=False, indent="\t")

# print(f'fixture 파일 생성 완료 / 저장 위치: {fixture_file_path}')
