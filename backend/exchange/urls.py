from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    path('<str:fromCountry>/<str:toCountry>/<int:price>/', views.exchange),
]

