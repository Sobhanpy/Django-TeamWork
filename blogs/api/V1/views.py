from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serialize import postSerializer, postDetailSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status



@api_view()
def post_api_view(request):
    post = Post.objects.filter(status=True)
    post_serilize = postSerializer(post, many=True)
    return Response(post_serilize.data)




@api_view(["GET", "POST", "PUT", "DELETE"])
def post_api_detail_view(request, pk):
    post = get_object_or_404(Post, id= str(pk))
    if request.method == "GET":
        post_serilize = postDetailSerializer(post)
        return Response(post_serilize.data)
    elif request.method == "POST":
        post_serilize = postDetailSerializer(data=request.data)
        if post_serilize.is_valid():
            post_serilize.save()
            return Response(post_serilize.data)
        else:
            return Response(post_serilize.errors)
    elif request.method == "PUT":
        post_serilize = postDetailSerializer(Post, data=request.data)
        post_serilize.is_valid(raise_exception=True)
        post_serilize.save()
        return Response(post_serilize.data)
    elif request.method == "DELETE":
        post.delete()
        return Response("Post deleted", status=status.HTTP_204_NO_CONTENT)