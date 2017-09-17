from django import template
from django.urls import reverse
from django.utils.html import escape

register = template.Library()


@register.inclusion_tag('nav/navlink.html', takes_context=True)
def navlink(context, url_name, anchor_text):
    current_url = context['request'].path
    nav_url = reverse(url_name)

    is_active = nav_url == current_url
    li_attr = 'class=active' if is_active else ''

    return {
        'url': nav_url,
        'anchor_text': escape(anchor_text),
        'attr': li_attr
    }
