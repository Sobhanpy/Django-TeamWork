from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serialize import PortfolioSerializer, PortfolioDetailSerializer
from ...models import Portfolio
from django.shortcuts import get_object_or_404
from rest_framework import status



@api_view()
def portfolios_api_view(request):
    portfolio = Portfolio.objects.filter(status=True)
    portfolio_serilize = PortfolioSerializer(portfolio, many=True)
    return Response(portfolio_serilize.data)




@api_view(["GET", "POST", "PUT", "DELETE"])
def portfolio_api_detail_view(request, pk):
    portfolio = get_object_or_404(Portfolio, id=pk)
    if request.method == "GET":
        portfolio_serilize = PortfolioDetailSerializer(portfolio)
        return Response(portfolio_serilize.data)
    elif request.method == "POST":
        portfolio_serilize = PortfolioDetailSerializer(data=request.data)
        if portfolio_serilize.is_valid():
            portfolio_serilize.save()
            return Response(portfolio_serilize.data)
        else:
            return Response(portfolio_serilize.errors)
    elif request.method == "PUT":
        portfolio_serilize = PortfolioDetailSerializer(Portfolio, data=request.data)
        portfolio_serilize.is_valid(raise_exception=True)
        portfolio_serilize.save()
        return Response(portfolio_serilize.data)
    elif request.method == "DELETE":
        portfolio.delete()
        return Response("portfolio deleted", status=status.HTTP_204_NO_CONTENT)