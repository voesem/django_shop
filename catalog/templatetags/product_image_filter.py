from django import template

register = template.Library()


@register.filter
def mediapath(path):
    return f'/media/{path}'


@register.simple_tag
def mediapath(path):
    return f'/media/{path}'
