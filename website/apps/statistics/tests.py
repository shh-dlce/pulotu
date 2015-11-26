"""
Tests for Statistics
"""
from django.test import TestCase
from django.contrib.auth.models import User
from website.apps.core.models import Language, Culture, Source

from website.apps.statistics import Statistic, AlreadyRegistered, InvalidMethod, InvalidField
from website.apps.statistics.models import StatisticalValue

class StatisticTest(TestCase):
    def setUp(self):
        self.editor = User.objects.create(username='admin')
        self.lang1 = Language.objects.create(language='A',classification='a, b',
                                             isocode='aaa', editor=self.editor)
        self.lang2 = Language.objects.create(language='B', classification='c, d, e',
                                             isocode='bbb', editor=self.editor)
        self.cult1 = Culture.objects.create(culture='Maori', slug='maori', editor=self.editor)
        
        # make sure we're clean (i.e. ignore whatever Statistic's are defined 
        # in the above imported models)
        self.statistic = Statistic()
        self.statistic.register("NLang", Language)
        self.statistic.register("NCulture", Culture)
        self.statistic.register("NSource", Source)
        
    def test_get_count(self):
        assert self.statistic._get_count(Language, 'id') == 2
        assert self.statistic._get_count(Culture, 'id') == 1
        
    def test_get_count_zero(self):
        assert self.statistic._get_count(Source, 'id') == 0
        
    def test_get_count_error(self):
        with self.assertRaises(InvalidField):
            self.statistic._get_count(Source, 'var') == 0
            
    def test_bad_statistic(self):
        with self.assertRaises(InvalidMethod):
            self.statistic.register("Bad Statistic", Language, method="NOTHING")
        
    def test_fail_register(self):
        with self.assertRaises(AlreadyRegistered):
            self.statistic.register("NLang", Language)
        
    def test_update(self):
        assert len(StatisticalValue.objects.all()) == 0
        self.statistic.update()
        assert len(StatisticalValue.objects.all()) == 3
        assert StatisticalValue.objects.filter(label="NLang")[0].value == 2
        assert StatisticalValue.objects.filter(label="NCulture")[0].value == 1
        assert StatisticalValue.objects.filter(label="NSource")[0].value == 0
    
    def test_get_all(self):
        """Tests the manager method .get_all"""
        self.statistic.update()
        # note the list comprehension is because .values_list returns a 
        # django.db.models.query.ValuesListQuerySet which is not a normal list
        assert [_ for _ in StatisticalValue.objects.get_all("NCulture")] == [1.0]
        assert [_ for _ in StatisticalValue.objects.get_all("NLang")] == [2.0]
    
    def test_get_all_ordering(self):
        """Tests the manager method .get_all ordering"""
        # create some
        self.statistic.update()
        for i in range(1,3):
            StatisticalValue.objects.create(
                label="NLang",
                model="what.ever",
                method="count",
                field="id",
                value = (2 + i)
            )
        # note the list comprehension is because .values_list returns a 
        # django.db.models.query.ValuesListQuerySet which is not a normal list
        assert [_ for _ in StatisticalValue.objects.get_all("NLang")] == [2.0, 3.0, 4.0]
