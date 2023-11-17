from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 url
    path('deposit/', views.deposit_list),
    # 정기예금 상세정보 url
    path('deposit/<str:fin_prdt_cd>/', views.deposit_detail),
    # 적금 url
    path('saving/', views.saving_list),
    # 적금 상세정보 url
    path('saving/<str:fin_prdt_cd>/', views.saving_detail),
]