from typing import Any

from .models import Portfolio

from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404





class PortfolioListView(ListView):
    
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'portfolio'
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Portfolio.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('teacher'):
            return Portfolio.objects.filter(client__info__email = self.kwargs.get('client'))
        elif self.request.GET.get('search'):
            return Portfolio.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Portfolio.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = PortfolioDetailView()
        return post_detail.post(request,*args,**kwargs)
    

    
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/PortfolioDetails.html'
    context_object_name = 'post'

    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     portfolios = Portfolio.objects.filter(status=True, id = int(self.kwargs.get['pk']))
    #     # portfolios = get_object_or_404(Portfolio, pk = int(self.request.GET.get['pk']))
    #     # context['portfolio'] = portfolios
    #     return portfolios