from django.db.models import Q
from django.utils.html import escape
from website.apps.core.models import Source
from ajax_select import LookupChannel


class source1(LookupChannel):

    model = Source

    def get_query(self, q, request):
        return Source.objects.filter(Q(author__icontains=q)).order_by('author')

    def get_result(self, obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.author

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return u"%s<div><i>" % (escape(obj.author))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"%s<div><i>" % (escape(obj.author))
