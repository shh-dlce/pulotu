from django.db import models

class StatisticManager(models.Manager):
    def get_all(self, label):
        return self.filter(label=label).values_list('value', flat=True).order_by('date')
    
    def get_all_with_dates(self, label):
        return self.filter(label=label).values_list('value', 'date').order_by('date')


class StatisticalValue(models.Model):
    """Stores Statistical information"""
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    label = models.CharField(max_length=128, db_index=True)
    model = models.CharField(max_length=255)
    method = models.CharField(max_length=12)
    field = models.CharField(max_length=32)
    value = models.FloatField()
    
    objects = StatisticManager()
    
    def __unicode__(self):
        return "%s = %s" % (self.label, self.value)
    
    class Meta:
        db_table = 'statistics'
        ordering = ['date', ]
        get_latest_by = 'date'
