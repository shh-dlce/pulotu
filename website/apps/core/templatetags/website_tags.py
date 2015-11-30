from django import template
from django.core.urlresolvers import resolve
from django.utils.safestring import mark_safe
from website.apps.core.models import Language
from website.apps.core.templatetags.ifinstalled import do_ifinstalled
import re

register = template.Library()


@register.filter(name='onlyone')
def only_one(listofobjects):
    return len(listofobjects) == 1


@register.filter(name='getkey')
def getkey(value, arg):
    return value[str(arg)]


@register.filter(name='firstletter')
def firstletter(phrase):
    return str(phrase)[0]


@register.filter(name='getsearchterm')
def searchterm(phrase):
    return phrase.partition('=')[2]


@register.filter(name='alphabetize')
def hasethonyms(listofobjects):
    return listofobjects.order_by('title')


@register.filter(name='hyphenate')
def hyphenate(phrase):
    return re.sub('[^0-9a-zA-Z]+', '-', phrase)


@register.filter(name='strs')
def strs(phrase):
    return str(phrase)


@register.filter(name='ethnologueunique')
def ethnologue_unique(langlist):
    return langlist.order_by('isocode').distinct('isocode')


@register.filter(name='nobrackets')
def nobrackets(phrase):
    if phrase[0] is '(':
        return phrase.partition('(')[1]
    else:
        try:
            return phrase.partition('(')[0]
        except:
            return phrase


@register.filter(name='ethnologue')
def link_ethnologue(lang):
    """Links to the Ethnologue"""
    if isinstance(lang, Language) and lang.isocode:
        return "http://www.ethnologue.com/language/%s" % lang.isocode
    else:
        return ""


@register.filter
def link_abvd(lang):
    """Links to the ABVD"""
    if isinstance(lang, Language) and lang.abvdcode:
        return "http://language.psy.auckland.ac.nz/austronesian/language.php?id=%s" % lang.abvdcode
    else:
        return ""


@register.filter
def link_olac(lang):
    """Links to the OLAC project"""
    if isinstance(lang, Language) and lang.isocode:
        return "http://search.language-archives.org/search.html?q=%s" % lang.isocode
    else:
        return ""


@register.filter
def link_llmap(lang):
    """Links to LLMap"""
    if isinstance(lang, Language) and lang.isocode:
        return "http://llmap.org/languages/%s.html" % lang.isocode
    else:
        return ""


@register.filter
def link_multitree(lang):
    """Links to MultiTree"""
    if isinstance(lang, Language) and lang.isocode:
        return "http://multitree.org/codes/%s" % lang.isocode
    else:
        return ""


@register.filter
def link_glottolog(lang):
    """Links to Glottolog"""
    if isinstance(lang, Language) and lang.isocode:
        return "http://glottolog.org/resource/languoid/iso/%s" % lang.isocode
    else:
        return ""


@register.filter
def language_map(lang):
    """Embeds a link to LLMap"""
    WIDTH = 400
    HEIGHT = 300

    if isinstance(lang, Language) and lang.isocode:
        return mark_safe("""
        <img src="http://llmap.org/language/%s.png?width=%d&height=%d" alt="Map of %s: courtesy of LL-MAP" />
        """ % (lang.isocode, WIDTH, HEIGHT, unicode(lang)))
    else:
        return ""


def active(context, view):
    try:
        resolved = resolve(context['request'].path_info)
    except KeyError:
        return ''

    if resolved.view_name == view:
        return ' class="active" '
    else:
        return ''


register.simple_tag(takes_context=True)(active)
register.tag('ifinstalled', do_ifinstalled)
