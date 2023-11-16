from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 url
    path('deposit/', views.deposit_list),
    # 정기적금 url
    path('saving/', views.saving_list),
]