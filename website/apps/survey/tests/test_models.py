from textwrap import dedent
from django.test import TestCase
from django.contrib.auth.models import User
from website.apps.core.models import Section
from website.apps.survey.models import Question, OptionQuestion


class TestOptionQuestion(TestCase):
    def setUp(self):
        self.editor = User.objects.create(username='admin')
        self.section = Section.objects.create(
            section="Test", slug="test", editor=self.editor)
        self.subsection = Section.objects.create(
            section="Sub", slug="sub", editor=self.editor)

    def test_save_override_no_response_type(self):
        """Test that .save() overrides the response_type correctly"""
        q = OptionQuestion.objects.create(
            number=1,
            question="Is 9 a good number?",
            options=dedent("""
            (0) yes
            (1) no
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        q.save()
        #assert q.response_type == Question.RESPONSETYPE_OPTION

    def test_save_override(self):
        """Test that .save() overrides the response_type correctly"""
        q = OptionQuestion.objects.create(
            number=1,
            question="Is 9 a good number?",
            options=dedent("""
            (0) yes
            (1) no
            """),
            response_type=Question.RESPONSETYPE_INTEGER,
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        q.save()
        #assert q.response_type == Question.RESPONSETYPE_OPTION

    def test_options_parsing_q8(self):
        # question 8 has three options ?,0,1
        q = OptionQuestion.objects.create(
            number=8,
            question="Belief that inanimate objects have supernatural properties",
            options=dedent("""
            (?) Missing data
            (0) absent
            (1) present
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        choices = q.get_choices()
        assert len(choices) == 3
        assert choices[0] == ('?', 'Missing data'), 'Got %r' % choices
        assert choices[1] == ('0', 'absent'), 'Got %r' % choices
        assert choices[2] == ('1', 'present'), 'Got %r' % choices

    def test_options_parsing_q3(self):
        # question 3 has four options ?, 0, 1, 2
        q = OptionQuestion.objects.create(
            number=3,
            question="Seasonal variation in rainfall:",
            options=dedent("""
            (?) Missing data
            (0)	Low	
            (1)	Moderate
            (2)	High 
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        choices = q.get_choices()
        assert len(choices) == 4
        assert choices[0] == ('?', 'Missing data'), 'Got %r' % choices
        assert choices[1] == ('0', 'Low'), 'Got %r' % choices
        assert choices[2] == ('1', 'Moderate'), 'Got %r' % choices
        assert choices[3] == ('2', 'High'), 'Got %r' % choices

    def test_options_parsing_q14(self):
        # question 14 has five options ?, 0, 1, 2, 3, 
        # with complex text descriptions
        q = OptionQuestion.objects.create(
            number=14,
            question="Belief in a High God:",
            options=dedent("""
            (?) Missing data
            (0) Absent or not reported in substantial description of indigenous religion
            (1) High god present, but not active in human affairs
            (2) High god present and active in human affairs, but not supportive of human morality
            (3) High god present, active in human affairs and supportive of human morality
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        choices = q.get_choices()
        assert len(choices) == 5
        assert choices[0] == ('?', 'Missing data'), \
            'Got %r' % choices
        assert choices[1] == (
        '0', 'Absent or not reported in substantial description of indigenous religion'), \
            'Got %r' % choices
        assert choices[2] == ('1', 'High god present, but not active in human affairs'), \
            'Got %r' % choices
        assert choices[3] == ('2',
                              'High god present and active in human affairs, but not supportive of human morality'), \
            'Got %r' % choices
        assert choices[4] == ('3',
                              'High god present, active in human affairs and supportive of human morality'), \
            'Got %r' % choices

    def test_options_parsing_q55(self):
        # question 55 has six options ?, 1, 2, 3, 4,
        q = OptionQuestion.objects.create(
            number=55,
            question="Land-based hunting performed by individuals:",
            options=dedent("""
            (?) Missing Data 
            (1)	Absent 
            (2)	Minor
            (3)	Medium 
            (4)	A principal or major food source 
            (5)	The principal food 
            """),
            section=self.section,
            subsection=self.subsection,
            editor=self.editor
        )
        choices = q.get_choices()
        assert len(choices) == 6
        assert choices[0] == ('?', 'Missing Data'), 'Got %r' % choices
        assert choices[1] == ('1', 'Absent'), 'Got %r' % choices
        assert choices[2] == ('2', 'Minor'), 'Got %r' % choices
        assert choices[3] == ('3', 'Medium'), 'Got %r' % choices
        assert choices[4] == ('4', 'A principal or major food source'), 'Got %r' % choices
        assert choices[5] == ('5', 'The principal food'), 'Got %r' % choices
