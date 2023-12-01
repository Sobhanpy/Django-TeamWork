from rest_framework import serializers
from ...models import *


class postSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "category", "image", "author", "status"]




class postDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'