from django import template

register = template.Library()
from main.models import ImageModel


@register.filter
def get(Image,name):
    return Image.filter(title=str(name))[0].mainimage.url
