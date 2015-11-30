# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from website.apps.statistics import statistic


class Command(BaseCommand):
    args = ''
    help = 'Updates all the defined statistics in the database'

    def handle(self, *args, **options):
        statistic.update()
