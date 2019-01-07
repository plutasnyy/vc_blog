from django import template

register = template.Library()


@register.filter(name='get')
def get(images, name):
    return images.filter(title=str(name))[0].mainimage.url
