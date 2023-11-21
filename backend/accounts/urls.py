from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('duplicateID/', views.duplicateID),
    path('get_portfolioData/', views.get_portfolioData),
    path('input_portfolioData/', views.input_portfolioData),
    path('check_password/', views.check_password)
]

