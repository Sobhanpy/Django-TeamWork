from rest_framework import serializers
from ...models import *


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ["id", "title", "price", "category", "image1", "image2", "image3"]




class PortfolioDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ["id", "title", "price", "category", "image1", "image2", "image3", "client_url", "client", "content", "status"]