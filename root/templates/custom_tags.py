from django import template
from root.models import Services,Team,Category,Price
from accounts.models import CustomeUser


register = template.Library()


@register.simple_tag
def service():
    service = Services.objects.filter(status=True)[:4]
    return service


@register.simple_tag
def team():
    member = Team.objects.filter(status=True)
    return member


@register.simple_tag
def category():
    category = Category.objects.all()
    return category

@register.simple_tag
def service():
    service = Services.objects.filter(status=True)
    return service

@register.simple_tag
def price():
    price = Price.objects.all()