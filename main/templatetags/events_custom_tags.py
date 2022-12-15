from django import template

register = template.Library()

@register.filter
def reslash (value):
    return value.replace('/', '%2F')