from django.urls import path, include
from .views import *


app_name = 'api-v1'

urlpatterns = [
    path("Posts/", post_api_view,name='posts'),
    path("Post-detail/<int:pk>", post_api_detail_view,name='post-detail'),

]