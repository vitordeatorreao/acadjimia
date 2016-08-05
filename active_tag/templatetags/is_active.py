# coding=utf-8

# code by Stack Overflow user semente:
# http://stackoverflow.com/users/116001/semente
# can be found here http://stackoverflow.com/questions/9793576/how-to-render-menu-with-one-active-item-with-dry

import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    print("pattern: %s\tpath: %s" % (pattern, path))
    if re.search(pattern, path):
        return 'active'
    return ''
