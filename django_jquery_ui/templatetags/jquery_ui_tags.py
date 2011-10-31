import os
from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def include_jquery_ui():
    return """<script type='text/javascript' src='%s'></script>
<link type='text/css' href='%s' rel='Stylesheet' />""" % (os.path.join(getattr(settings, 'STATIC_URL'), 'jquery-ui', 'jquery-ui-1.8.16.custom.min.js'),
                                                          os.path.join(getattr(settings, 'STATIC_URL'), 'jquery-ui', 'jquery-ui-1.8.16.custom.css'))
