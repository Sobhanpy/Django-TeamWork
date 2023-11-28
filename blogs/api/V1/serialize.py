from rest_framework import serializers
from ...models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "category", "image", "author", "status"]




class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "category", "image", "author", "content", "tag", "counted_views", "status"]