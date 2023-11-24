from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    path('currency/<str:fromCountry>/<int:price>/<str:st_date>/<str:howlong>/', views.exchange),
]

