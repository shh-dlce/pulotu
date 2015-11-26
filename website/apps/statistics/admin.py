from django.contrib import admin
from website.apps.statistics.models import StatisticalValue

class StatisticalValueAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('label', 'model', 'value')
    list_filter = ('label', 'model',)
    ordering = ('date',)

admin.site.register(StatisticalValue, StatisticalValueAdmin)
