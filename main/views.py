from typing import Any
from django.db import models
from django.shortcuts import render , get_object_or_404, redirect
from .models import Portfolio, Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentForm, ReplyForm
from django.contrib import messages
from root.models import NewsLetter
from root.forms import NewsLetterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




class PortfolioListView(ListView):
    
    template_name = 'main/Portfolio.html'
    context_object_name = 'portfolio'
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Portfolio.objects.filter(category__name=self.kwargs.get('cat'))
        elif self.kwargs.get('teacher'):
            return Portfolio.objects.filter(client__info__username = self.kwargs.get('client'))
        elif self.request.GET.get('search'):
            return Portfolio.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Portfolio.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = PortfolioDetailView()
        return post_detail.post(request,*args,**kwargs)
    

    
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'main/Portfolio-details.html'
    context_object_name = 'portfolio'

    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        id_list = []
        portfolios = Portfolio.objects.filter(status=True)
        for cr in portfolios:
            id_list.append(cr.id)

        id_list.reverse()
            
        if id_list[0] == self.kwargs.get('object').id : 
            
            next_portfolio = Portfolio.objects.get(id=id_list[1])
            previous_portfolio = None

        elif id_list[-1] == self.kwargs.get('object').id : 
            
            next_portfolio = None
            previous_portfolio = Portfolio.objects.get(id = id_list[-2])

        else:  
            next_portfolio = Portfolio.objects.get(id=id_list[id_list.index(kwargs.get('object').id)+1])
            previous_portfolio = Portfolio.objects.get(id=id_list[id_list.index(kwargs.get('object').id)-1])
        context['next_portfolio'] = next_portfolio
        context['previous_portfolio'] = previous_portfolio
        return context