from django import template
from django.utils.safestring import mark_safe

import markdown as md

register = template.Library()

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)


@register.filter(name='markdown')
def markdown_filter(value):
    # nl2br keeps single line breaks, so plain-text notes written before
    # the markdown switch still render the way they were typed.
    return mark_safe(md.markdown(
        value or '',
        extensions=['fenced_code', 'tables', 'sane_lists', 'nl2br'],
    ))
