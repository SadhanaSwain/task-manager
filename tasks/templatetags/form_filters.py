from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})

@register.filter
def pluck(list_of_dicts, key):
    return [d.get(key) for d in list_of_dicts]