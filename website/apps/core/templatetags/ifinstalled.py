from django import template
from django.conf import settings

class InstalledAppNode(template.Node):
    child_nodelists = ('nodelist_true', 'nodelist_false')
    
    def __init__(self, app, nodelist_true, nodelist_false):
        self.app = app
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        
    def __repr__(self):
        return "<IfInstalledNode>"
        
    def render(self, context):
        if self.app in settings.INSTALLED_APPS:
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)


def do_ifinstalled(parser, token):
    """
    Outputs the contents of the block if the app is in INSTALLED_APPS

    Examples::

        {% ifinstalled "my.app" %}
            ...
        {% endifinstalled %}

        {% ifinstalled "my.app" %}
            ...
        {% else %}
            ...
        {% endifinstalled %}
    """
    bits = list(token.split_contents())
    if len(bits) != 2:
        raise TemplateSyntaxError("%r takes two arguments" % bits[0])
    end_tag = 'end' + bits[0]
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = template.NodeList()
    return InstalledAppNode(bits[1][1:-1], nodelist_true, nodelist_false)
