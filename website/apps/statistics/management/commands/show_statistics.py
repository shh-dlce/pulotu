# -*- coding: utf-8 -*-
from django.db import transaction
from django.core.management.base import BaseCommand

from website.apps.statistics import statistic

class Command(BaseCommand):
    args = ''
    help = 'Displays all the defined statistics in the database'
    
    def handle(self, *args, **options):
        s = statistic.update(save=False)
        for label, value in s.items():
            print(u"%s %s" % (label.ljust(30), value))