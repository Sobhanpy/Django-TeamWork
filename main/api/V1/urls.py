from django.urls import path, include
from .views import *


app_name = 'api-v1'

urlpatterns = [
    path("portfolios/", portfolios_api_view,name='portfolios'),
    path("portfolio-detail/<int:pk>" ,portfolio_api_detail_view,name='portfolio-detail'),

]