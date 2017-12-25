from django import template

register = template.Library()
from main.models import ImageModel


@register.filter(name='get')
def get(Images,name):
    return Images.filter(title=str(name))[0].mainimage.url
