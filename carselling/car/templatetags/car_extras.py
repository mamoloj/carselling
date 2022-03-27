from atexit import register
from base64 import encode
from django import template

register = template.Library()

@register.simple_tag
def page_filter_url(value,field_name,urlencode=None):
    url = '?{0}={1}'.format(field_name,value)

    if urlencode:
        qs = urlencode.split('&')
        filtered_qs = filter(lambda p: p.split('=')[0]!=field_name,qs)
        encoded_qs = '&'.join(filtered_qs)
        url = '{0}&{1}'.format(url,encoded_qs)

    return url